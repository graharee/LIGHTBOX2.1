import os
import pandas as pd
import numpy as np


CSV_FOLDER = "csv_tests"
OUTPUT_FILE = "visible_light_lookup_table.csv"


def build_targets_mlux():
    targets = []

    # 0 lux to 1 lux = 0 to 1000 mlux, 1 mlux increments
    targets += list(range(0, 1001, 1))

    # 1 lux to 5 lux = 1000 to 5000 mlux, 10 mlux increments
    targets += list(range(1010, 5001, 10))

    # 5 lux to 25 lux = 5000 to 25000 mlux, 25 mlux increments
    targets += list(range(5025, 25001, 25))

    # 25 lux to 100 lux = 25000 to 100000 mlux, 100 mlux increments
    targets += list(range(25100, 100001, 100))

    # 100 lux to 300 lux = 100000 to 300000 mlux, 1 lux increments
    targets += list(range(100000, 300001, 1000))

    return sorted(set(targets))


TARGETS_MLUX = build_targets_mlux()


def load_all_csvs(folder):
    all_rows = []

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".csv"):
            continue

        path = os.path.join(folder, filename)
        df = pd.read_csv(path)

        required_columns = [
            "formation_name",
            "current_ma",
            "pwm_percent",
            "measured_mlux",
        ]

        for col in required_columns:
            if col not in df.columns:
                raise RuntimeError(
                    f"{filename} is missing required column: {col}"
                )

        df = df[required_columns].copy()
        df["source_file"] = filename

        all_rows.append(df)

    if not all_rows:
        raise RuntimeError(f"No CSV files found in folder: {folder}")

    combined = pd.concat(all_rows, ignore_index=True)

    combined["current_ma"] = pd.to_numeric(combined["current_ma"], errors="coerce")
    combined["pwm_percent"] = pd.to_numeric(combined["pwm_percent"], errors="coerce")
    combined["measured_mlux"] = pd.to_numeric(combined["measured_mlux"], errors="coerce")

    combined = combined.dropna(
        subset=[
            "formation_name",
            "current_ma",
            "pwm_percent",
            "measured_mlux",
        ]
    )

    combined = combined.sort_values(
        ["formation_name", "current_ma", "pwm_percent"]
    )

    return combined


def find_best_setting(df, target_mlux):
    best_candidate = None
    best_error = float("inf")

    group_cols = ["formation_name", "current_ma"]

    for group_key, group in df.groupby(group_cols):
        formation_name, current_ma = group_key

        group = group.sort_values("measured_mlux")

        measured = group["measured_mlux"].to_numpy()
        pwms = group["pwm_percent"].to_numpy()

        if len(measured) < 2:
            continue

        min_mlux = measured.min()
        max_mlux = measured.max()

        # This formation/current combo cannot reach the target
        if not (min_mlux <= target_mlux <= max_mlux):
            continue

        estimated_pwm_float = np.interp(target_mlux, measured, pwms)

        # Since your GUI/CAN command probably sends integer PWM values,
        # round to the nearest whole PWM percent.
        estimated_pwm = int(round(estimated_pwm_float))

        estimated_mlux = np.interp(
            estimated_pwm,
            pwms,
            measured
        )

        error = abs(estimated_mlux - target_mlux)

        lower_idx = np.searchsorted(measured, target_mlux) - 1
        upper_idx = lower_idx + 1

        lower_idx = max(0, lower_idx)
        upper_idx = min(len(measured) - 1, upper_idx)

        lower_row = group.iloc[lower_idx]
        upper_row = group.iloc[upper_idx]

        if error < best_error:
            best_candidate = {
                "target_mlux": target_mlux,
                "formation_name": formation_name,
                "current_ma": int(current_ma),
                "pwm_percent": estimated_pwm,
                "estimated_mlux": round(float(estimated_mlux), 3),
                "error_mlux": round(float(error), 3),
                "lower_measured_mlux": round(float(lower_row["measured_mlux"]), 3),
                "lower_pwm_percent": int(lower_row["pwm_percent"]),
                "upper_measured_mlux": round(float(upper_row["measured_mlux"]), 3),
                "upper_pwm_percent": int(upper_row["pwm_percent"]),
                "method": "interpolated",
            }

            best_error = error

    return best_candidate


def build_lookup_table(df):
    lookup_rows = []

    for target_mlux in TARGETS_MLUX:
        result = find_best_setting(df, target_mlux)

        if result is not None:
            lookup_rows.append(result)
        else:
            lookup_rows.append({
                "target_mlux": target_mlux,
                "formation_name": "",
                "current_ma": "",
                "pwm_percent": "",
                "estimated_mlux": "",
                "error_mlux": "",
                "lower_measured_mlux": "",
                "lower_pwm_percent": "",
                "upper_measured_mlux": "",
                "upper_pwm_percent": "",
                "method": "no_match_found",
            })

    return pd.DataFrame(lookup_rows)


def export_python_lookup_table(lookup_df, output_py_file):
    usable = lookup_df[lookup_df["method"] != "no_match_found"].copy()

    with open(output_py_file, "w", encoding="utf-8") as f:
        f.write("# Auto-generated visible light lookup table\n")
        f.write("# Generated from measured CSV sweep data\n\n")
        f.write("VISIBLE_LIGHT_LOOKUP = {\n")

        for _, row in usable.iterrows():
            target = int(row["target_mlux"])
            formation = row["formation_name"]
            current = int(row["current_ma"])
            pwm = int(row["pwm_percent"])

            f.write(f"    {target}: {{\n")
            f.write(f'        "formation_name": "{formation}",\n')
            f.write(f'        "current_ma": {current},\n')
            f.write(f'        "pwm_percent": {pwm},\n')
            f.write(f"    }},\n")

        f.write("}\n")


def main():
    measured_df = load_all_csvs(CSV_FOLDER)

    measured_df.to_csv("combined_measured_results.csv", index=False)

    lookup_df = build_lookup_table(measured_df)

    lookup_df.to_csv(OUTPUT_FILE, index=False)

    export_python_lookup_table(
        lookup_df,
        "visible_light_lookup_table.py"
    )

    print("Done.")
    print(f"Loaded measured rows: {len(measured_df)}")
    print(f"Saved combined measurements to: combined_measured_results.csv")
    print(f"Saved full lookup CSV to: {OUTPUT_FILE}")
    print(f"Saved Python lookup table to: visible_light_lookup_table.py")
    print(
        "Targets with no match:",
        (lookup_df["method"] == "no_match_found").sum()
    )


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk


RED = "#d92525"
GREEN = "#16a34a"
RED_DARK = "#b91c1c"
BG = "#eef2f6"
CARD = "#ffffff"
CARD_SOFT = "#f7f9fc"
BORDER = "#d6dde8"
TEXT = "#1f2937"
MUTED = "#6b7280"
VALUE_BG = "#f8fafc"
BUTTON_BG = "#e8edf5"
BUTTON_ACTIVE = "#dbe4f0"
BLUE = "#2563eb"
BLUE_SOFT = "#dbeafe"
TAB_BG = "#dde6f2"


class StatusDot(tk.Canvas):
    def __init__(self, parent, size=18, color=RED, bg=CARD, **kwargs):
        super().__init__(
            parent,
            width=size,
            height=size,
            highlightthickness=0,
            bd=0,
            bg=bg,
            **kwargs,
        )
        self.size = size
        self.oval = self.create_oval(2, 2, size - 2, size - 2, fill=color, outline="#b91c1c", width=1)

    def set_color(self, color, outline=None):
        self.itemconfigure(self.oval, fill=color, outline=outline or color)


class LightboxGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Magna Lightbox 2.1")
        self.geometry("1560x900")
        self.minsize(1460, 860)
        self.configure(bg=BG)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self._configure_styles()

        self.source_dots = {}
        self.source_states = {}

        self._build_header()
        self._build_notebook()

    def _configure_styles(self):
        self.style.configure("App.TFrame", background=BG)

        self.style.configure(
            "Notebook.TNotebook",
            background=BG,
            borderwidth=0,
            tabmargins=(10, 0, 0, 0),
        )
        self.style.configure(
            "Notebook.TNotebook.Tab",
            background=TAB_BG,
            foreground="#334155",
            font=("Segoe UI", 14, "bold"),
            padding=(22, 12),
            borderwidth=1,
        )
        self.style.map(
            "Notebook.TNotebook.Tab",
            background=[("selected", CARD)],
            foreground=[("selected", TEXT)],
        )

        self.style.configure(
            "Primary.TButton",
            font=("Segoe UI", 13, "bold"),
            padding=(24, 14),
            background=BUTTON_BG,
            foreground=TEXT,
            relief="flat",
            borderwidth=1,
            focuscolor="none",
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", BUTTON_ACTIVE), ("pressed", BUTTON_ACTIVE)],
        )

        self.style.configure(
            "Apply.TButton",
            font=("Segoe UI", 13, "bold"),
            padding=(22, 12),
            background=BLUE,
            foreground="white",
            relief="flat",
            borderwidth=0,
            focuscolor="none",
        )
        self.style.map(
            "Apply.TButton",
            background=[("active", "#1d4ed8"), ("pressed", "#1d4ed8")],
        )

        self.style.configure(
            "Set.TButton",
            font=("Segoe UI", 13, "bold"),
            padding=(22, 12),
            background=BLUE,
            foreground="white",
            relief="flat",
            borderwidth=0,
            focuscolor="none",
        )
        self.style.map(
            "Set.TButton",
            background=[("active", "#1d4ed8"), ("pressed", "#1d4ed8")],
        )

        self.style.configure(
            "TEntry",
            padding=10,
            fieldbackground="white",
            foreground=TEXT,
            bordercolor="#b9c4d3",
            lightcolor="#b9c4d3",
            darkcolor="#b9c4d3",
            insertcolor=TEXT,
        )

    def _build_header(self):
        header = tk.Frame(self, bg=RED, height=88)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Magna Lightbox 2.1",
            bg=RED,
            fg="white",
            font=("Segoe UI", 30, "bold"),
        ).pack(side="left", padx=24, pady=18)

        tk.Label(
            header,
            text="Control Interface",
            bg=RED,
            fg="#ffe5e5",
            font=("Segoe UI", 13, "bold"),
        ).pack(side="right", padx=24)

    def _build_notebook(self):
        outer = ttk.Frame(self, style="App.TFrame", padding=(18, 16, 18, 18))
        outer.pack(fill="both", expand=True)

        notebook = ttk.Notebook(outer, style="Notebook.TNotebook")
        notebook.pack(fill="both", expand=True)

        basic = ttk.Frame(notebook, style="App.TFrame")
        advanced = ttk.Frame(notebook, style="App.TFrame")
        notebook.add(basic, text="Basic")
        notebook.add(advanced, text="Advanced")

        self._build_basic_tab(basic)
        self._build_advanced_tab(advanced)

    def _card(self, parent, title, row, column, columnspan=1, rowspan=1, padx=10, pady=10):
        shell = tk.Frame(parent, bg=BORDER, highlightthickness=0)
        shell.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=padx, pady=pady)

        container = tk.Frame(shell, bg=CARD)
        container.pack(fill="both", expand=True, padx=1, pady=1)

        header = tk.Frame(container, bg="#f3f6fb", height=46)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text=title,
            bg="#f3f6fb",
            fg=TEXT,
            font=("Segoe UI", 15, "bold"),
        ).pack(anchor="w", padx=18, pady=11)

        body = tk.Frame(container, bg=CARD)
        body.pack(fill="both", expand=True, padx=18, pady=18)
        return body

    def _value_box(self, parent, text="0", width=170, height=54, font=("Segoe UI", 15, "bold")):
        frame = tk.Frame(parent, bg="#b9c4d3", width=width, height=height)
        frame.pack_propagate(False)
        inner = tk.Frame(frame, bg=VALUE_BG)
        inner.pack(fill="both", expand=True, padx=1, pady=1)
        tk.Label(inner, text=text, bg=VALUE_BG, fg="#0f2d5c", font=font).pack(expand=True)
        return frame

    def _square_button(self, parent, text, fg=BLUE, bg=BLUE_SOFT, size=86):
        btn = tk.Button(
                parent,
                text=text,
                font=("Segoe UI", 24, "bold"),
                fg=fg,
                bg=bg,
                activebackground="#c7dcff",
                activeforeground=fg,
                relief="flat",
                bd=0,
                cursor="hand2",
                width=1,
                height=1,
                padx=24,
                pady=1,
        )
        return btn

    def _build_basic_tab(self, tab):
        for i in range(12):
            tab.columnconfigure(i, weight=1, uniform="basic")
        for i in range(7):
            tab.rowconfigure(i, weight=1)

        source = self._card(tab, "Select Light Source", 0, 1, columnspan=10)
        self._build_source_selector(source)

        ambient = self._card(tab, "Visible Ambient Adjustment", 1, 0, columnspan=7, rowspan=3)
        self._build_adjustment_section(ambient, "Target Ambient Value")

        status = self._card(tab, "System Status", 1, 7, columnspan=5, rowspan=3)
        self._build_status_section(status)

        glare = self._card(tab, "Visible Glare Adjustment", 4, 0, columnspan=7, rowspan=3)
        self._build_adjustment_section(glare, "Target Glare Value")

        optometer = self._card(tab, "Optometer Readings", 4, 7, columnspan=5, rowspan=3)
        self._build_optometer_section(optometer)

    def _build_source_selector(self, parent):
        self.source_buttons = {}
        for i in range(3):
            parent.columnconfigure(i, weight=1)

        for col, label in enumerate(["IR", "HEADLIGHT", "SUNLIGHT"]):
            tile = tk.Frame(parent, bg=CARD_SOFT, highlightbackground="#e5eaf1", highlightthickness=1, padx=12, pady=12)
            tile.grid(row=0, column=col, padx=12, sticky="nsew")
            tile.columnconfigure(0, weight=0)
            tile.columnconfigure(1, weight=1)
            tile.columnconfigure(2, weight=0)

            dot = StatusDot(tile, size=18, color=RED, bg=CARD_SOFT)
            dot.grid(row=0, column=0, padx=(12, 14), pady=10)
            self.source_dots[label] = dot

            tk.Label(
                tile,
                text=label,
                bg=CARD_SOFT,
                fg=TEXT,
                font=("Segoe UI", 14, "bold"),
                anchor="w",
            ).grid(row=0, column=1, sticky="w")

            button = tk.Button(
                tile,
                text="Enable",
                font=("Segoe UI", 12, "bold"),
                bg=BUTTON_BG,
                fg=TEXT,
                activebackground=BUTTON_ACTIVE,
                activeforeground=TEXT,
                relief="flat",
                bd=0,
                cursor="hand2",
                width=12,
                padx=12,
                pady=10,
                command=lambda name=label: self._toggle_source(name),
            )

            button.grid(row=0, column=2, padx=(20, 10), pady=6, sticky="e")
            self.source_buttons[label] = button
            self.source_states[label] = False

    def _toggle_source(self, source_name):
        current_state = self.source_states[source_name]

        if not current_state:
            self.source_dots[source_name].set_color(GREEN, "#15803d")
            self.source_buttons[source_name].configure(
                text="Disable",
                bg=BLUE,
                fg="white",
                activebackground="#1d4ed8",
                activeforeground="white",
                relief="sunken"
            )
            self.source_states[source_name] = True
        else:
            self.source_dots[source_name].set_color(RED, "#b91c1c")
            self.source_buttons[source_name].configure(
                text="Enable",
                bg=BUTTON_BG,
                fg=TEXT,
                activebackground=BUTTON_ACTIVE,
                activeforeground=TEXT,
                relief="flat"
            )
            self.source_states[source_name] = False

    def _build_adjustment_section(self, source_name):
        dot = self.source_dots.get(source_name)
        if dot is None:
            return
        current = dot.itemcget(dot.oval, "fill")
        if current.lower() == GREEN:
            dot.set_color(RED, "#b91c1c")
        else:
            dot.set_color(GREEN, "#15803d")

    def _build_adjustment_section(self, parent, label_text):
        parent.columnconfigure(0, weight=0)
        parent.columnconfigure(1, weight=1)
        parent.columnconfigure(2, weight=1)
        parent.columnconfigure(3, weight=0)
        parent.rowconfigure(0, weight=1)

        controls = tk.Frame(parent, bg=CARD)
        controls.grid(row=0, column=0, rowspan=3, sticky="ns", padx=(0, 18))

        plus = self._square_button(controls, "+")
        plus.pack(pady=(0, 12), ipadx=2, ipady=2)
        minus = self._square_button(controls, "−", fg="#475569", bg="#edf2f7")
        minus.pack(ipadx=2, ipady=2)

        tk.Label(parent, text=label_text, bg=CARD, fg=MUTED, font=("Segoe UI", 13)).grid(row=0, column=1, sticky="sw", pady=(8, 8))
        tk.Label(parent, text="Sent Value", bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=0, column=2, sticky="sw", pady=(8, 8))

        input_wrap = tk.Frame(parent, bg=CARD)
        input_wrap.grid(row=1, column=1, sticky="ew", padx=(0, 24))
        input_wrap.columnconfigure(0, weight=1)
        ttk.Entry(input_wrap, font=("Segoe UI", 14)).grid(row=0, column=0, sticky="ew")
        tk.Label(input_wrap, text="mlux", bg=CARD, fg="#42526b", font=("Segoe UI", 13)).grid(row=0, column=1, padx=(12, 0))

        sent_wrap = tk.Frame(parent, bg=CARD)
        sent_wrap.grid(row=1, column=2, columnspan=2, sticky="w")
        box = self._value_box(sent_wrap, text="0", width=220, height=56)
        box.pack(side="left")
        tk.Label(sent_wrap, text="mlux", bg=CARD, fg="#42526b", font=("Segoe UI", 13)).pack(side="left", padx=(14, 0))

        ttk.Button(parent, text="Set", style="Set.TButton").grid(row=2, column=1, sticky="w", pady=(18, 0), ipadx=8, ipady=4)

    def _build_status_section(self, parent):
        items = ["Connection Status", "CAN Bus Initialization", "Invalid Input"]
        for i, item in enumerate(items):
            row = tk.Frame(parent, bg=CARD)
            row.pack(fill="x", pady=10)
            StatusDot(row, size=18, color=RED, bg=CARD).pack(side="left", padx=(6, 14))
            tk.Label(row, text=item, bg=CARD, fg=TEXT, font=("Segoe UI", 14)).pack(side="left")

    def _build_optometer_section(self, parent):
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)

        for i, title in enumerate(["Ambient", "Glare"]):
            tile = tk.Frame(parent, bg=CARD_SOFT, highlightbackground="#e5eaf1")
            tile.grid(row=0, column=i, sticky="nsew", padx=8)
            tk.Label(tile, text=title, bg=CARD_SOFT, fg="#243b63", font=("Segoe UI", 15, "bold")).pack(pady=(22, 16))
            box = self._value_box(tile, text="0", width=180, height=68, font=("Segoe UI", 24, "bold"))
            box.pack()
            tk.Label(tile, text="mlux", bg=CARD_SOFT, fg=MUTED, font=("Segoe UI", 15)).pack(pady=(14, 18))

    def _build_advanced_tab(self, tab):
        for i in range(12):
            tab.columnconfigure(i, weight=1, uniform="adv")
        for i in range(7):
            tab.rowconfigure(i, weight=1)

        node = self._card(tab, "LED Node Control", 0, 0, columnspan=7, rowspan=6)
        fan = self._card(tab, "Fan Speed Adjustment", 0, 7, columnspan=5, rowspan=2)

        self._build_node_control(node)
        self._build_fan_control(fan)

    def _entry_with_unit(self, parent, row, col, unit=None, padx=(0, 20)):
        wrap = tk.Frame(parent, bg=CARD)
        wrap.grid(row=row, column=col, sticky="ew", padx=padx)
        wrap.columnconfigure(0, weight=1)
        ttk.Entry(wrap, font=("Segoe UI", 13)).grid(row=0, column=0, sticky="ew")
        if unit:
            tk.Label(wrap, text=unit, bg=CARD, fg="#42526b", font=("Segoe UI", 13)).grid(row=0, column=1, padx=(12, 0))

    def _build_node_control(self, parent):
        for i in range(4):
            parent.columnconfigure(i, weight=1)

        tk.Label(parent, text="Node Address", bg=CARD, fg=TEXT, font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w")
        self._entry_with_unit(parent, 0, 1)
        tk.Label(parent, text="Sent Value", bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=0, column=2, sticky="w")
        self._value_box(parent, text="0", width=170, height=54).grid(row=0, column=3, sticky="w")

        btns = tk.Frame(parent, bg=CARD)
        btns.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(24, 18))
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=1)
        ttk.Button(btns, text="Turn ON", style="Primary.TButton").grid(row=0, column=0, sticky="ew", padx=(0, 12))
        ttk.Button(btns, text="Turn OFF", style="Primary.TButton").grid(row=0, column=1, sticky="ew", padx=(12, 0))

        self._advanced_row(parent, 2, "Temperature Request", button_text="Get", unit="°C")
        self._advanced_row(parent, 3, "Current", unit="mA")
        self._advanced_row(parent, 4, "PWM", unit="%")

    def _advanced_row(self, parent, row, title, unit, button_text=None):
        sep = tk.Frame(parent, bg="#edf2f7", height=1)
        sep.grid(row=row * 2 - 1, column=0, columnspan=4, sticky="ew", pady=(8, 14))

        tk.Label(parent, text=title, bg=CARD, fg=TEXT, font=("Segoe UI", 11, "bold")).grid(row=row * 2, column=0, sticky="w")
        if button_text:
            ttk.Button(parent, text=button_text, style="Primary.TButton").grid(row=row * 2, column=1, sticky="w")
        else:
            self._entry_with_unit(parent, row * 2, 1)
        if row > 2:
            tk.Label(parent, text="Sent Value", bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=row * 2, column=2, sticky="w")
        else:
            tk.Label(parent, bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=row * 2, column=2, sticky="w")

        wrap = tk.Frame(parent, bg=CARD)
        wrap.grid(row=row * 2, column=3, sticky="w")
        self._value_box(wrap, text="0", width=150, height=52, font=("Segoe UI", 17, "bold")).pack(side="left")
        tk.Label(wrap, text=unit, bg=CARD, fg="#42526b", font=("Segoe UI", 13)).pack(side="left", padx=(12, 0))

    def _build_fan_control(self, parent):
        parent.columnconfigure(0, weight=0)
        parent.columnconfigure(1, weight=1)
        parent.columnconfigure(2, weight=1)

        controls = tk.Frame(parent, bg=CARD)
        controls.grid(row=0, column=0, rowspan=3, sticky="ns", padx=(0, 18))
        plus = self._square_button(controls, "+")
        plus.pack(pady=(6, 12))
        minus = self._square_button(controls, "−", fg="#475569", bg="#edf2f7")
        minus.pack()

        tk.Label(parent, text="Fan Input", bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=0, column=1, sticky="sw", pady=(6, 8))
        tk.Label(parent, text="Sent Value", bg=CARD, fg=MUTED, font=("Segoe UI", 15)).grid(row=0, column=2, sticky="sw", pady=(6, 8))

        ttk.Entry(parent, font=("Segoe UI", 14)).grid(row=1, column=1, sticky="ew", padx=(0, 22))
        self._value_box(parent, text="0", width=170, height=56).grid(row=1, column=2, sticky="w")
        ttk.Button(parent, text="Apply", style="Apply.TButton").grid(row=2, column=1, sticky="w", pady=(16, 0))


if __name__ == "__main__":
    app = LightboxGUI()
    app.mainloop()

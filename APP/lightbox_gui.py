'''
    File: lightbox_gui.py
    Desciption: This is the file creates the tkinter GUI-- GUI LOGIC ONLY

    By: Reegan Graham
'''
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
        self.iconbitmap("lightbox.png")
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
        ).pack(expand=True, pady=18)

    def _build_notebook(self):
        outer = ttk.Frame(self, style="App.TFrame", padding=(18, 16, 18, 18))
        outer.pack(fill="both", expand=True)

        notebook = ttk.Notebook(outer, style="Notebook.TNotebook")
        notebook.pack(fill="both", expand=True)

        basic = ttk.Frame(notebook, style="App.TFrame")
        advanced = ttk.Frame(notebook, style="App.TFrame")
        calibration  = ttk.Frame(notebook, style="App.TFrame")

        notebook.add(basic, text="Basic")
        notebook.add(advanced, text="Advanced")
        notebook.add(calibration, text="Calibration")

        self._build_basic_tab(basic)
        self._build_advanced_tab(advanced)
        self._build_calibration_tab(calibration)

    def _card(self, parent, title, row, column, columnspan=1, rowspan=1, padx=10, pady=10):
        shell = tk.Frame(parent, bg=BORDER)
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
        self._build_adjustment_section(ambient, "Visible Ambient Value")

        status = self._card(tab, "Faults", 1, 7, columnspan=5, rowspan=3)
        self._build_status_section(status)

        glare = self._card(tab, "Visible Glare Adjustment", 4, 0, columnspan=7, rowspan=3)
        self._build_adjustment_section(glare, "Visible Glare Value")

        optometer = self._card(tab, "Optometer Readings", 4, 7, columnspan=5, rowspan=3)
        self._build_optometer_section(optometer)

    def _build_source_selector(self, parent):
        self.source_buttons = {}

        labels = ["IR (850nm)", "IR (940nm)", "HEADLIGHT", "SUNLIGHT"]

        for i in range(4):
            parent.columnconfigure(i, weight=1, uniform="node")

        for col, label in enumerate(labels):
            tile = tk.Frame(parent, bg=CARD, padx=8, pady=8)
            tile.grid(row=0, column=col, padx=10, sticky="nsew")
            tile.columnconfigure(0, weight=0)
            tile.columnconfigure(1, weight=1)
            tile.columnconfigure(2, weight=0)

            dot = StatusDot(tile, size=18, color=RED, bg=CARD)
            dot.grid(row=0, column=0, padx=(4, 10), pady=6)
            self.source_dots[label] = dot

            tk.Label(
                tile,
                text=label,
                bg=CARD,
                fg=TEXT,
                font=("Segoe UI", 13, "bold"),
                anchor="w",
            ).grid(row=0, column=1, sticky="w")

            button = tk.Button(
                tile,
                text="ON",
                font=("Segoe UI", 11, "bold"),
                bg=BUTTON_BG,
                fg=TEXT,
                activebackground=BUTTON_ACTIVE,
                activeforeground=TEXT,
                relief="raised",
                bd=1,
                cursor="hand2",
                width=5,
                padx=6,
                pady=4,
                command=lambda name=label: self._toggle_source(name),
            )
            button.grid(row=0, column=2, padx=(10, 0), sticky="e")

            self.source_buttons[label] = button
            self.source_states[label] = False

    def _toggle_source(self, source_name):
        current_state = self.source_states[source_name]

        if not current_state:
            self.source_dots[source_name].set_color(GREEN, "#15803d")
            self.source_buttons[source_name].configure(
                text="OFF",
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
                text="ON",
                bg=BUTTON_BG,
                fg=TEXT,
                activebackground=BUTTON_ACTIVE,
                activeforeground=TEXT,
                relief="raised"
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
        self.status_dots = {}

        items = [
            ("connection", "Connection Status"),
            ("can_init", "CAN Bus Failed Initialization"),
            ("invalid_input", "Invalid Input"),
            ("calibration_status", "Calibration Status"),
        ]

        for key, label_text in items:
            row = tk.Frame(parent, bg=CARD)
            row.pack(fill="x", pady=10)

            dot = StatusDot(row, size=18, color=RED, bg=CARD)
            dot.pack(side="left", padx=(6, 14))

            tk.Label(
                row,
                text=label_text,
                bg=CARD,
                fg=TEXT,
                font=("Segoe UI", 14)
            ).pack(side="left")

            # store the SAME dot you displayed
            self.status_dots[key] = dot

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

        node = self._card(tab, "LED Node Adjustment", 0, 0, columnspan=7, rowspan=7)
        fan = self._card(tab, "Fan PWM Adjustment", 0, 7, columnspan=5, rowspan=2)

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

        # ---------------- Top Row: Node Address / LED Address ----------------
        tk.Label(
            parent,
            text="Node\nAddress",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 13, "bold"),
            justify="center"
        ).grid(row=0, column=0, sticky="nsew", pady=(8, 4))

        self.node_address_entry = ttk.Entry(parent, font=("Segoe UI", 14))
        self.node_address_entry.grid(row=0, column=1, sticky="", padx=(40, 20), pady=(0, 12), ipady=6)

        tk.Label(
            parent, 
            text="LED\nAddress", 
            bg=CARD, 
            fg=TEXT, 
            font=("Segoe UI", 13, "bold"), 
            justify="center"
        ).grid(row=0, column=2, sticky="nsew", pady=(8, 12))

        self.led_address_entry = ttk.Entry(parent, font=("Segoe UI", 14))
        self.led_address_entry.grid(row=0, column=3, sticky="",  padx=(20, 10), pady=(0, 12), ipady=6)

        # ---------------- ON / OFF Buttons ----------------
        sep1 = tk.Frame(parent, bg="#edf2f7", height=1)
        sep1.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(2, 18))

        btns = tk.Frame(parent, bg=CARD)
        btns.grid(row=2, column=0, columnspan=4, sticky="ew", pady=(0, 18))
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=1)

        ttk.Button(
            btns,
            text="ON",
            style="Primary.TButton",
            command=self._handle_turn_on
        ).grid(row=0, column=0, sticky="ew", padx=(20, 20), ipadx=8, ipady=14)

        ttk.Button(
            btns,
            text="OFF",
            style="Primary.TButton",
            command=self._handle_turn_off
        ).grid(row=0, column=1, sticky="ew", padx=(20, 20), ipadx=8, ipady=14)

        # ---------------- Temperature Request ----------------
        sep2 = tk.Frame(parent, bg="#edf2f7", height=1)
        sep2.grid(row=3, column=0, columnspan=4, sticky="ew", pady=(0, 18))

        tk.Label(parent, text="Temperature Request", bg=CARD, fg=TEXT, font=("Segoe UI", 13, "bold")).grid(
            row=4, column=0, sticky="w", pady=(4, 10)
        )

        tk.Button(
            parent,
            text="GET",
            font=("Segoe UI", 13, "bold"),
            bg=BUTTON_BG,
            fg=TEXT,
            activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT,
            relief="raised",
            bd=1,
            cursor="hand2",
            width=5,
            pady=8
        ).grid(row=4, column=1, sticky="w", padx=(0, 20), pady=(4, 10))

        temp_wrap = tk.Frame(parent, bg=CARD)
        temp_wrap.grid(row=4, column=2, columnspan=2, sticky="w", pady=(4, 10))
        self._value_box(temp_wrap, text="0", width=170, height=56, font=("Segoe UI", 20, "bold")).pack(side="left")
        tk.Label(temp_wrap, text="°C", bg=CARD, fg=TEXT, font=("Segoe UI", 18, "bold")).pack(side="left", padx=(12, 0))

        # ---------------- Current ----------------
        sep3 = tk.Frame(parent, bg="#edf2f7", height=1)
        sep3.grid(row=5, column=0, columnspan=4, sticky="ew", pady=(0, 18))

        tk.Label(parent, text="Current", bg=CARD, fg=TEXT, font=("Segoe UI", 13, "bold")).grid(
            row=6, column=0, sticky="w", pady=(4, 10)
        )

        current_entry_wrap = tk.Frame(parent, bg=CARD)
        current_entry_wrap.grid(row=6, column=1, sticky="ew", padx=(0, 20), pady=(4, 10))
        current_entry_wrap.columnconfigure(0, weight=1)
        self.current_entry = ttk.Entry(current_entry_wrap, font=("Segoe UI", 14))
        self.current_entry.grid(row=0, column=0, sticky="ew")

        tk.Label(current_entry_wrap, text="mA", bg=CARD, fg=MUTED, font=("Segoe UI", 12)).grid(row=0, column=1, padx=(8,0))
        current_sent_wrap = tk.Frame(parent, bg=CARD)
        current_sent_wrap.grid(row=6, column=3, sticky="w", pady=(4, 10))

        self._value_box(current_sent_wrap, text="0", width=170, height=56, font=("Segoe UI", 20, "bold")).pack(side="left")

        tk.Label(
            current_sent_wrap,
            text="mA",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 12)
        ).pack(side="left", padx=(10, 0))

        # ---------------- PWM ----------------
        sep4 = tk.Frame(parent, bg="#edf2f7", height=1)
        sep4.grid(row=7, column=0, columnspan=4, sticky="ew", pady=(0, 18))

        tk.Label(parent, text="PWM", bg=CARD, fg=TEXT, font=("Segoe UI", 13, "bold")).grid(
            row=8, column=0, sticky="w", pady=(4, 10)
        )

        pwm_entry_wrap = tk.Frame(parent, bg=CARD)
        pwm_entry_wrap.grid(row=8, column=1, sticky="ew", padx=(0, 20), pady=(4, 10))
        pwm_entry_wrap.columnconfigure(0, weight=1)
        self.pwm_entry = ttk.Entry(pwm_entry_wrap, font=("Segoe UI", 14))
        self.pwm_entry.grid(row=0, column=0, sticky="ew")

        tk.Label(pwm_entry_wrap, text="%", bg=CARD, fg=MUTED, font=("Segoe UI", 12)).grid(row=0, column=1, padx=(8,0))

        pwm_sent_wrap = tk.Frame(parent, bg=CARD)
        pwm_sent_wrap.grid(row=8, column=3, sticky="w", pady=(4, 10))

        self._value_box(pwm_sent_wrap, text="0", width=170, height=56, font=("Segoe UI", 20, "bold")).pack(side="left")

        tk.Label(
            pwm_sent_wrap,
            text="%",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 14)
        ).pack(side="left", padx=(10, 0))
        
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

    def set_status_dot(self, name, color):
        self.status_dots[name].set_color(color)

    def _handle_turn_on(self):
        node_text = self.node_address_entry.get()
        self.controller.turn_on_node(node_text)

    def _handle_turn_off(self):
        node_text = self.node_address_entry.get()
        self.controller.turn_off_node(node_text)

    def _build_calibration_tab(self, tab):
        for i in range(12):
            tab.columnconfigure(i, weight=1, uniform="cal")
        for i in range(8):
            tab.rowconfigure(i, weight=0)

        # keep everything near the top like the mockup
        tab.rowconfigure(3, weight=1)

        cal_card = self._card(tab, "Calibration", 0, 0, columnspan=7, rowspan=3, padx=10, pady=10)
        self._build_calibration_main(cal_card)

        notes_card = self._card(tab, "Calibration Notes", 0, 7, columnspan=5, rowspan=2, padx=10, pady=10)
        self._build_calibration_notes(notes_card)

    def _build_calibration_main(self, parent):
        for i in range(2):
            parent.columnconfigure(i, weight=1, uniform="calmain")
        for i in range(3):
            parent.rowconfigure(i, weight=0)

        # -------- Row 1: Start Calibration --------
        tk.Label(
            parent,
            text="Start Calibration",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 18, "bold")
        ).grid(row=0, column=0, sticky="w", padx=(40, 20), pady=(16, 16))

        self.start_cal_button = tk.Button(
            parent,
            text="START",
            font=("Segoe UI", 24, "bold"),
            bg="#d9d9d9",
            fg="black",
            activebackground="#cfcfcf",
            activeforeground="black",
            relief="raised",
            bd=1,
            cursor="hand2",
            width=20,
            pady=6,
            command=self._handle_start_calibration
        )
        self.start_cal_button.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(12, 12))

        tk.Frame(parent, bg="#edf2f7", height=1).grid(
            row=1, column=0, columnspan=2, sticky="ew", pady=(0, 0)
        )

        # -------- Row 2: Status --------
        status_label = tk.Label(
            parent,
            text="Status",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 18, "bold")
        )
        status_label.grid(row=2, column=0, sticky="w", padx=(40, 20), pady=(18, 18))

        self.cal_status_box = self._value_box(
            parent,
            text="IN PROGRESS",
            width=390,
            height=85,
            font=("Segoe UI", 18, "bold")
        )
        self.cal_status_box.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(12, 12))

        tk.Frame(parent, bg="#edf2f7", height=1).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(0, 0)
        )

        # -------- Row 3: Faults --------
        faults_label = tk.Label(
            parent,
            text="Faults",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 18, "bold")
        )
        faults_label.grid(row=4, column=0, sticky="w", padx=(40, 20), pady=(18, 18))

        self.cal_faults_box = self._value_box(
            parent,
            text="FAILED",
            width=390,
            height=85,
            font=("Segoe UI", 18, "bold")
        )
        self.cal_faults_box.grid(row=4, column=1, sticky="w", padx=(10, 20), pady=(12, 12))

    def _build_calibration_notes(self, parent):
        notes_text = (
            "* Ensure GPIB-USB-HS is connected\n"
            "* DO NOT try to adjust lightbox until\n"
            "  calibration is complete\n"
            "* other notes needed"
        )

        tk.Label(
            parent,
            text=notes_text,
            justify="left",
            anchor="nw",
            bg=CARD,
            fg="black",
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="nw", padx=12, pady=10)

    def _handle_start_calibration(self):
        print("Calibration started")

    def _value_box(self, parent, text="0", width=170, height=54, font=("Segoe UI", 15, "bold")):
        frame = tk.Frame(parent, bg="#b9c4d3", width=width, height=height)
        frame.pack_propagate(False)
        frame.grid_propagate(False)

        inner = tk.Frame(frame, bg=VALUE_BG)
        inner.pack(fill="both", expand=True, padx=1, pady=1)

        label = tk.Label(inner, text=text, bg=VALUE_BG, fg="#0f2d5c", font=font)
        label.pack(expand=True)

        frame.value_label = label
        return frame
    
if __name__ == "__main__":
    app = LightboxGUI()
    app.mainloop()

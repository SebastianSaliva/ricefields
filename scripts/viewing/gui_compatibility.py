import tkinter as tk
from tkinter import font as tkfont, ttk


class CompatibilityMatrix(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Desktop Environment Compatibility Matrix")
        self.configure(bg="white")

        # Define data
        self.distributions = ["MINT", "UBUNTU", "DEBIAN", "MANJARO", "FEDORA", "ARCH"]
        self.environments = [
            "GNOME",
            "KDE_PLASMA",
            "XFCE",
            "CINNAMON",
            "MATE",
            "LXQT",
            "BUDGIE",
            "LXDE",
            "DDE",
            "PANTHEON",
        ]

        # Compatibility matrix (2 = Default/Official, 1 = Available/Community, 0 = Via Package Manager Only)
        self.compatibility = {
            "GNOME": [1, 2, 2, 2, 2, 1],
            "KDE_PLASMA": [1, 2, 2, 2, 2, 1],
            "XFCE": [2, 2, 2, 2, 2, 1],
            "CINNAMON": [2, 0, 0, 1, 1, 1],
            "MATE": [2, 2, 1, 1, 2, 1],
            "LXQT": [0, 2, 1, 1, 2, 1],
            "BUDGIE": [0, 1, 0, 0, 0, 1],
            "LXDE": [0, 0, 1, 0, 0, 1],
            "DDE": [0, 0, 0, 0, 0, 1],
            "PANTHEON": [0, 0, 0, 0, 0, 1],
        }

        # Color mapping
        self.colors = {
            2: "#90EE90",  # Light green for Default/Official
            1: "#FFE4B5",  # Light orange for Community/Available
            0: "#ADD8E6",  # Light blue for Package Manager
        }

        self.create_widgets()

    def get_compatibility_color(self, value):
        return self.colors.get(value, "#FFFFFF")  # White for unknown values

    def get_compatibility_text(self, value):
        texts = {2: "Default/Official", 1: "Community/Available", 0: "Package Manager"}
        return texts.get(value, "N/A")

    def create_tooltip(self, widget, text):
        def on_enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 20

            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")

            label = tk.Label(
                self.tooltip,
                text=text,
                justify="left",
                background="#ffffe0",
                relief="solid",
                borderwidth=1,
            )
            label.pack()

        def on_leave(event):
            if hasattr(self, "tooltip"):
                self.tooltip.destroy()

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create canvas and scrollable frame
        canvas = tk.Canvas(main_frame, background="white")
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create header row
        header_label = tk.Label(
            scrollable_frame,
            text="DE / Distro",
            borderwidth=1,
            relief="solid",
            width=15,
            bg="white",
            font=("Arial", 10, "bold"),
        )
        header_label.grid(row=0, column=0, sticky="nsew")

        # Create distribution headers
        for j, dist in enumerate(self.distributions, 1):
            label = tk.Label(
                scrollable_frame,
                text=dist,
                borderwidth=1,
                relief="solid",
                width=10,
                bg="white",
                font=("Arial", 10, "bold"),
            )
            label.grid(row=0, column=j, sticky="nsew")

        # Create matrix cells
        for i, env in enumerate(self.environments, 1):
            # Environment names
            env_label = tk.Label(
                scrollable_frame,
                text=env,
                borderwidth=1,
                relief="solid",
                width=15,
                bg="white",
                font=("Arial", 10),
            )
            env_label.grid(row=i, column=0, sticky="nsew")

            # Compatibility values
            for j, value in enumerate(self.compatibility[env], 1):
                cell = tk.Label(
                    scrollable_frame,
                    text=str(value),
                    borderwidth=1,
                    relief="solid",
                    width=10,
                    bg=self.get_compatibility_color(value),
                )
                cell.grid(row=i, column=j, sticky="nsew")

                # Add tooltip
                self.create_tooltip(cell, self.get_compatibility_text(value))

        # Create legend
        legend_frame = ttk.Frame(scrollable_frame, padding="10")
        legend_frame.grid(
            row=len(self.environments) + 1,
            column=0,
            columnspan=len(self.distributions) + 1,
            pady=10,
        )

        legend_title = tk.Label(
            legend_frame, text="Legend:", font=("Arial", 10, "bold")
        )
        legend_title.pack(anchor="w")

        for value, text in [
            (2, "Default/Official Support"),
            (1, "Community/Available Support"),
            (0, "Available via Package Manager"),
        ]:
            legend_item = tk.Frame(legend_frame)
            legend_item.pack(anchor="w", pady=2)

            color_box = tk.Label(
                legend_item, text="", width=2, bg=self.get_compatibility_color(value)
            )
            color_box.pack(side="left", padx=5)

            text_label = tk.Label(legend_item, text=f"{value} = {text}")
            text_label.pack(side="left")

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


if __name__ == "__main__":
    app = CompatibilityMatrix()
    app.mainloop()

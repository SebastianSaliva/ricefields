import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk


class RiceCreatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("R.I.C.E. Creator")
        self.geometry("800x600")

        # Variables to store selections
        self.selected_env = tk.StringVar()
        self.selected_distro = tk.StringVar()

        # Define arrays (copied from creation_script.py)
        self.DISTROS = ["MINT", "UBUNTU", "DEBIAN", "MANJARO", "ARCH", "FEDORA"]
        self.ENVIRONMENTS = [
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

        self.create_gui()

    def create_gui(self):
        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame, text="R.I.C.E. Creator", font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create two frames for environments and distributions
        env_frame = ttk.LabelFrame(main_frame, text="Environments", padding="10")
        env_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        distro_frame = ttk.LabelFrame(main_frame, text="Distributions", padding="10")
        distro_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        # Configure weights for the frames
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)

        # Add environment buttons
        for i, env in enumerate(self.ENVIRONMENTS):
            btn = ttk.Radiobutton(
                env_frame,
                text=env.replace("_", " "),
                value=env,
                variable=self.selected_env,
                command=self.update_execute_button,
            )
            btn.grid(row=i, column=0, pady=2, padx=5, sticky="w")

        # Add distribution buttons
        for i, distro in enumerate(self.DISTROS):
            btn = ttk.Radiobutton(
                distro_frame,
                text=distro,
                value=distro,
                variable=self.selected_distro,
                command=self.update_execute_button,
            )
            btn.grid(row=i, column=0, pady=2, padx=5, sticky="w")

        # Status frame
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Selection display
        self.selection_label = ttk.Label(
            status_frame, text="Please select an environment and distribution"
        )
        self.selection_label.pack(pady=5)

        # Execute button
        self.execute_button = ttk.Button(
            status_frame,
            text="Execute Script",
            command=self.execute_script,
            state="disabled",
        )
        self.execute_button.pack(pady=5)

        # Create All button
        self.create_all_button = ttk.Button(
            status_frame, text="Create All Combinations", command=self.create_all
        )
        self.create_all_button.pack(pady=5)

    def update_execute_button(self):
        env = self.selected_env.get()
        distro = self.selected_distro.get()

        if env and distro:
            self.selection_label.config(
                text=f"Selected: {env.replace('_', ' ')}/{distro}"
            )
            self.execute_button.config(state="normal")
        else:
            self.selection_label.config(
                text="Please select an environment and distribution"
            )
            self.execute_button.config(state="disabled")

    def execute_script(self):
        env = self.selected_env.get()
        distro = self.selected_distro.get()

        if not env or not distro:
            messagebox.showerror(
                "Error", "Please select both an environment and a distribution"
            )
            return

        try:
            # Get the directory of the current script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_dir, "creation_script.py")

            # Run the creation script with the selected options
            result = subprocess.run(
                [sys.executable, script_path, f"{env}/{distro}"],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                messagebox.showinfo(
                    "Success", f"Successfully created structure for {env}/{distro}"
                )
            else:
                messagebox.showerror(
                    "Error", f"Error creating structure: {result.stderr}"
                )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def create_all(self):
        try:
            # Get the directory of the current script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_dir, "creation_script.py")

            # Run the creation script with 'all' parameter
            result = subprocess.run(
                [sys.executable, script_path, "all"], capture_output=True, text=True
            )

            if result.returncode == 0:
                messagebox.showinfo(
                    "Success", "Successfully created structure for all combinations"
                )
            else:
                messagebox.showerror(
                    "Error", f"Error creating structure: {result.stderr}"
                )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = RiceCreatorGUI()
    # Configure style
    style = ttk.Style()
    style.configure("TButton", padding=6)
    style.configure("TRadiobutton", padding=3)
    style.configure("TLabelframe", padding=10)

    app.mainloop()

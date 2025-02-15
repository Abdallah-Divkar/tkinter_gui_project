import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        # Setup
        super().__init__()
        self.title("Centennial College")
        self.geometry("400x300")
        self.resizable(True, True)
        self.configure(bg="cyan")

        # Define styles
        self.style = ttk.Style()
        self.style.configure("TFrame", background="cyan")
        self.style.configure("TLabel", background="cyan")

        # Main frame
        self.main_frame = ttk.Frame(self, padding=10, relief="ridge", style="TFrame")
        self.main_frame.pack(expand=True, fill="both")

        # Title
        self.title_label = ttk.Label(self.main_frame, text="ICET Student Survey", font=("Arial", 14, "bold"), style="TLabel")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=5)

        # Name
        ttk.Label(self.main_frame, text="Full Name:", style="TLabel").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=2)

        # Residency
        ttk.Label(self.main_frame, text="Residency:", style="TLabel").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.residency_var = tk.StringVar(value="dom")
        self.dom_radio = ttk.Radiobutton(self.main_frame, text="Domestic", variable=self.residency_var, value="dom")
        self.intl_radio = ttk.Radiobutton(self.main_frame, text="International", variable=self.residency_var, value="intl")
        self.dom_radio.grid(row=2, column=1, sticky="w", padx=50, pady=2)
        self.intl_radio.grid(row=3, column=1, sticky="w", padx=50, pady=2)

        # Program
        ttk.Label(self.main_frame, text="Program:", style="TLabel").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        self.program_var = tk.StringVar()
        self.program_combo = ttk.Combobox(self.main_frame, textvariable=self.program_var, values=["AI", "Gaming", "Health", "Software"])
        self.program_combo.grid(row=4, column=1, padx=50, pady=2)
        self.program_var.set("AI")  # Set default value

        # Courses
        ttk.Label(self.main_frame, text="Courses:", style="TLabel").grid(row=5, column=0, sticky="nw", padx=5, pady=2)
        self.course1_var = tk.StringVar(value="")
        self.course2_var = tk.StringVar(value="")
        self.course3_var = tk.StringVar(value="")
        self.course1_cb = ttk.Checkbutton(self.main_frame, text="Programming I", variable=self.course1_var, onvalue="COMP100", offvalue="")
        self.course2_cb = ttk.Checkbutton(self.main_frame, text="Web Page Design", variable=self.course2_var, onvalue="COMP213", offvalue="")
        self.course3_cb = ttk.Checkbutton(self.main_frame, text="Software Engineering", variable=self.course3_var, onvalue="COMP120", offvalue="")
        self.course1_cb.grid(row=5, column=1, sticky="w", padx=50, pady=2)
        self.course2_cb.grid(row=6, column=1, sticky="w", padx=50, pady=2)
        self.course3_cb.grid(row=7, column=1, sticky="w", padx=50, pady=2)

if __name__ == "__main__":
    app = App()
    app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centennial College")
        self.geometry("400x300")
        self.resizable(True, True)
        self.configure(bg="lightgreen")

        # Define styles
        self.style = ttk.Style()
        self.style.configure("TFrame", background="lightgreen")
        self.style.configure("TLabel", background="lightgreen")

        # Main frame (expands when window resizes)
        self.main_frame = tk.Frame(self, padx=10, pady=10, bg="lightgreen", relief="ridge")
        self.main_frame.pack(expand=True, fill="both")

        # Configure grid to expand
        for i in range(9):  # Rows
            self.main_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):  # Columns
            self.main_frame.grid_columnconfigure(j, weight=1)

        # Title
        self.title_label = tk.Label(self.main_frame, text="ICET Student Survey", font=("Arial", 14, "bold"),
                                    bg="lightgreen", fg="black")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew")

        # Name
        tk.Label(self.main_frame, text="Full Name:", bg="lightgreen", fg="black").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.name_entry = tk.Entry(self.main_frame, fg="black")
        self.name_entry.grid(row=1, column=1, padx=5, pady=2, sticky="nsew")

        # Residency
        tk.Label(self.main_frame, text="Residency:", bg="lightgreen", fg="black").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.residency_var = tk.StringVar(value="dom")
        self.dom_radio = tk.Radiobutton(self.main_frame, text="Domestic", variable=self.residency_var, value="dom", bg="lightgreen", fg="black")
        self.intl_radio = tk.Radiobutton(self.main_frame, text="International", variable=self.residency_var, value="intl", bg="lightgreen", fg="black")
        self.dom_radio.grid(row=2, column=1, padx=10, pady=2, sticky="w")
        self.intl_radio.grid(row=3, column=1, padx=10, pady=2, sticky="w")

        # Program
        tk.Label(self.main_frame, text="Program:", bg="lightgreen", fg="black").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.program_var = tk.StringVar()
        self.program_combo = ttk.Combobox(self.main_frame, textvariable=self.program_var, values=["AI", "Gaming", "Health", "Software"], width=22)
        self.program_combo.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        self.program_var.set("AI")

        # Courses
        tk.Label(self.main_frame, text="Courses:", bg="lightgreen", fg="black").grid(row=5, column=0, padx=5, pady=2, sticky="w")
        self.course1_var = tk.StringVar(value="")
        self.course2_var = tk.StringVar(value="")
        self.course3_var = tk.StringVar(value="")
        self.course1_cb = tk.Checkbutton(self.main_frame, text="Programming I", variable=self.course1_var, onvalue="COMP100", offvalue="", bg="lightgreen", fg="black")
        self.course2_cb = tk.Checkbutton(self.main_frame, text="Web Page Design", variable=self.course2_var, onvalue="COMP213", offvalue="", bg="lightgreen", fg="black")
        self.course3_cb = tk.Checkbutton(self.main_frame, text="Software Engineering", variable=self.course3_var, onvalue="COMP120", offvalue="", bg="lightgreen", fg="black")
        self.course1_cb.grid(row=5, column=1, padx=10, pady=2, sticky="w")
        self.course2_cb.grid(row=6, column=1, padx=10, pady=2, sticky="w")
        self.course3_cb.grid(row=7, column=1, padx=10, pady=2, sticky="w")

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="lightgreen")
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")
        self.button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.ok_button = tk.Button(self.button_frame, text="OK", command=self.validate_and_show)
        self.ok_button.grid(row=0, column=0, padx=5, sticky="nsew")

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=0, column=1, padx=5, sticky="nsew")

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.quit)
        self.exit_button.grid(row=0, column=2, padx=5, sticky="nsew")

    def validate_and_show(self):
        """Validates form inputs before displaying details."""
        name = self.name_entry.get().strip()
        program = self.program_var.get().strip()
        courses = [self.course1_var.get(), self.course2_var.get(), self.course3_var.get()]
        selected_courses = [c for c in courses if c]

        if not name:
            messagebox.showerror("Error", "Full Name cannot be empty.")
            return
        if not program:
            messagebox.showerror("Error", "Please select a program.")
            return
        if not selected_courses:
            messagebox.showerror("Error", "At least one course must be selected.")
            return

        details = f"Name: {name}\nResidency: {'Domestic' if self.residency_var.get() == 'dom' else 'International'}\nProgram: {program}\nCourses: {', '.join(selected_courses)}"
        messagebox.showinfo("Information", details)

    def reset_fields(self):
        """Clears all input fields."""
        self.name_entry.delete(0, tk.END)
        self.residency_var.set("dom")
        self.program_var.set("AI")
        self.course1_var.set("")
        self.course2_var.set("")
        self.course3_var.set("")


if __name__ == "__main__":
    app = App()
    app.mainloop()

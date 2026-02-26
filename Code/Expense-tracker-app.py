from tkinter import *
from tkinter import ttk, messagebox
from expense_logic import validate_expense


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense-tracker")
        self.is_fullscreen = True
        self.attributes('-fullscreen', True)
        self.configure(bg="#2c3e50")

        self.expenses = []

        self.setup_styles()
        self.create_layout()

        self.bind("<Escape>", self.toggle_fullscreen)

    def show_add_expenses_window(self):
        self.amount.grid(row=0, column=0, padx=20, pady=20, ipadx=10, ipady=10)
        self.date.grid(column=0, row=1, padx=20, pady=20)
        self.type_of_expense.grid(column=0, row=2, padx=20, pady=20)
        self.note_label.grid(column=0, row=3, padx=20, pady=20)

        self.amount_entry.grid(column=1, row=0, padx=20, pady=20)
        self.date_entry.grid(column=1, row=1, padx=20, pady=20)
        self.type_dropdown.grid(column=1, row=2, padx=20, pady=20)
        self.note_entry.grid(column=1, row=3, padx=20, pady=20)

        self.save_button.grid(column=0, row=4, columnspan=2, pady=20)

    def setup_add_expenses_window(self):
        self.add_expenses_window = Toplevel(self)
        self.add_expenses_window.title("Add an expense")
        self.add_expenses_window.geometry(
            f"1000x700+{self.winfo_screenwidth() // 2 - 1000 // 2}+{self.winfo_screenheight() // 2 - 700 // 2}"
        )
        self.add_expenses_window.focus_force()
        self.add_expenses_window.grab_set()
        self.add_expenses_window.configure(bg="#34495e")

        self.amount_value = StringVar()
        self.date_value = StringVar()
        self.note_value = StringVar()
        self.selected_type = StringVar(value="select an option")

        self.amount = ttk.Label(self.add_expenses_window, text="Amount spent")
        self.date = ttk.Label(self.add_expenses_window, text="Select a date")
        self.type_of_expense = ttk.Label(self.add_expenses_window, text="Select a type")
        self.note_label = ttk.Label(self.add_expenses_window, text="Note")

        self.amount_entry = ttk.Entry(self.add_expenses_window, textvariable=self.amount_value)
        self.date_entry = ttk.Entry(self.add_expenses_window, textvariable=self.date_value)
        self.note_entry = ttk.Entry(self.add_expenses_window, textvariable=self.note_value)

        self.options = ["select an option", "Food", "Clothing", "Medicine", "video games", "Custom"]
        self.type_dropdown = ttk.OptionMenu(
            self.add_expenses_window, self.selected_type, *self.options
        )

        self.save_button = ttk.Button(
            self.add_expenses_window,
            text="Save Expense",
            command=self.save_expense
        )

    def create_add_expenses_window(self):
        self.setup_add_expenses_window()
        self.show_add_expenses_window()

    def save_expense(self):
        try:
            amount = int(self.amount_value.get())
            category = self.selected_type.get()
            date_string = self.date_value.get()
            note = self.note_value.get()

            validate_expense(amount, category, date_string, note)

            expense = {
                "amount": amount,
                "category": category,
                "date": date_string,
                "note": note
            }

            self.expenses.append(expense)

            messagebox.showinfo("Success", "Expense saved successfully")
            self.add_expenses_window.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes('-fullscreen', self.is_fullscreen)
        if not self.is_fullscreen:
            self.geometry("1920x1000")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure(
            "Title.TLabel",
            font=("Arial", 32, "bold"),
            foreground="#ecf0f1",
            background="#2c3e50"
        )
        style.configure(
            "TLabel",
            font=("Arial", 18, "bold"),
            foreground="#ecf0f1",
            background="#34495e"
        )
        style.configure(
            "TButton",
            font=("Arial", 12),
            padding=(15, 10),
        )
        style.configure(
            "Left.TFrame",
            background="#2c3e50"
        )
        style.configure(
            "Right.TFrame",
            background="#34495e"
        )

    def create_layout(self):
        self.title_label = ttk.Label(self, text="EXPENSE TRACKER", style="Title.TLabel")
        self.title_label.grid(pady=(30, 20))

        self.container = Frame(self, bg="#2c3e50")

        for i in (0, 5):
            self.container.columnconfigure(i, weight=1)
            self.container.rowconfigure(i, weight=1)

        self.container.grid(padx=50, pady=(0, 30))

        self.create_left_frame()
        self.create_right_frame()

    def create_left_frame(self):
        self.left_frame = Frame(self.container, bg="#3a546f", width=700, height=900)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=0)
        self.left_frame.grid(row=0, column=0, columnspan=4, padx=(0, 0), sticky="nsew")
        self.left_frame.grid_propagate(False)

        self.add_expense_btn = ttk.Button(
            self.left_frame,
            text="+ Add Expense",
            command=self.create_add_expenses_window
        )
        self.add_expense_btn.grid(row=0, column=0, sticky="nw", pady=(30, 10), padx=30)

        self.view_expenses_btn = ttk.Button(self.left_frame, text="View Expenses")
        self.view_expenses_btn.grid(row=1, column=0, sticky="nw", pady=10, padx=30)

        self.view_summary_btn = ttk.Button(self.left_frame, text="Monthly Summary")
        self.view_summary_btn.grid(row=2, column=0, sticky="nw", pady=10, padx=30)

        self.settings_button = ttk.Button(self.left_frame, text="Settings")
        self.settings_button.grid(row=3, column=0, sticky="nw", pady=10, padx=30)

        self.exit_btn = ttk.Button(self.left_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row=4, column=0, sticky="nw", pady=(30, 10), padx=30)

    def create_right_frame(self):
        self.right_frame = Frame(self.container, bg="#29445f", width=1200)
        self.right_frame.grid(row=0, column=5, padx=(0, 0), rowspan=1, sticky="nsew")
        self.right_frame.grid_propagate(False)

        self.calendar_label = ttk.Label(
            self.right_frame,
            text="CALENDAR",
            style="Heading.TLabel"
        )
        self.calendar_label.grid(row=0, column=1, pady=20, padx=500, sticky="nsew", columnspan=2)

        self.calendar_placeholder = Label(
            self.right_frame,
            text="Calendar is here",
            font=("Arial", 12),
            fg="#7f8c8d",
            bg="#34495e"
        )
        self.calendar_placeholder.grid(row=1, column=1, columnspan=5, pady=300)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

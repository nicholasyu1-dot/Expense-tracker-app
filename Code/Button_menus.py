
from tkinter import *
from tkinter import ttk, messagebox
from expense_logic import validate_expense


class Menu:

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


    def setup_add_expenses_window(self,expenses,screen):
        self.add_expenses_window = Toplevel(screen)
        self.add_expenses_window.title("Add an expense")
        self.add_expenses_window.geometry(
            f"1000x700+{screen.winfo_screenwidth() // 2 - 1000 // 2}+{screen.winfo_screenheight() // 2 - 700 // 2}"
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
            command=lambda: self.save_expense(expenses)
        )


    def create_add_expenses_window(self,expenses,screen):
        print(expenses)

        self.setup_add_expenses_window(expenses,screen)
        self.show_add_expenses_window()



    def save_expense(self,expenses):
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

            expenses.append(expense)

            messagebox.showinfo("Success", "Expense saved successfully")
            self.add_expenses_window.destroy()


        except ValueError as e:
            messagebox.showerror("Error", "Please enter values")




    def setup_view_expenses_window(self,expenses,screen):
        self.expenses = expenses



    def create_view_expenses_window(self,expenses,screen):
        self.setup_view_expenses_window(expenses,screen)
        self.show_view_expenses_window(screen)

    def show_view_expenses_window(self,screen):

        view_window = Toplevel(screen)
        view_window.title("Saved Expenses")
        view_window.geometry("900x500")

        view_window.focus_force()
        view_window.grab_set()

        view_window.configure(bg="#34495e")

        columns = ("amount", "category", "date", "note")
        tree = ttk.Treeview(view_window, columns=columns, show="headings")

        tree.heading("amount", text="Amount")
        tree.heading("category", text="Category")
        tree.heading("date", text="Date")
        tree.heading("note", text="Note")

        tree.column("amount", width=100)
        tree.column("category", width=150)
        tree.column("date", width=120)
        tree.column("note", width=400)

        for expense in self.expenses:
            tree.insert(
                "",
                "end",
                values=(
                    expense["amount"],
                    expense["category"],
                    expense["date"],
                    expense["note"]
                )
            )
        tree.pack(fill=BOTH, expand=True, padx=20, pady=20)

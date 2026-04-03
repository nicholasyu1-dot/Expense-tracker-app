from tkinter import *
from tkinter import ttk, messagebox
from expense_logic import validate_expense
import ctypes as ct




class Menu:
    def __init__(self):
        self.main_colour = "#34495e"
        self.border_colour = 0x00372716

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
        self.add_expenses_window.configure(bg=self.main_colour)
        self.change_title_bar(self.add_expenses_window, self.border_colour)

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

        view_window.configure(bg=self.main_colour)
        self.change_title_bar(view_window, self.border_colour)

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





    def setup_monthly_expenses_window(self,expenses,screen):
        self.monthly_expenses = expenses



    def create_monthly_expenses_window(self,expenses,screen):
        self.setup_monthly_expenses_window(expenses,screen)
        self.show_monthly_expenses_window(screen)

    def show_monthly_expenses_window(self,screen):

        monthly_window = Toplevel(screen)
        monthly_window.title("Monthly Expenses")
        monthly_window.geometry("900x500")

        monthly_window.focus_force()
        monthly_window.grab_set()

        monthly_window.configure(bg=self.main_colour)
        self.change_title_bar(monthly_window, self.border_colour)


        columns = ( "month","amount")
        tree = ttk.Treeview(monthly_window, columns=columns, show="headings")

        tree.heading("month", text="Month")

        tree.heading("amount", text="Amount")

        tree.column("month", width=120)
        tree.column("amount", width=100)

        print(self.monthly_expenses)
        for month,expenses in self.monthly_expenses.items():
            print(expenses)
            total_expenses = 0
            for expense in expenses:
                print(expense[0])

                total_expenses+=expense[0]
            tree.insert(
                "",
                "end",
                values=(
                    month,
                    total_expenses
                )
            )
        tree.pack(fill=BOTH, expand=True, padx=20, pady=20)




    def show_settings_window(self,screen,global_style,border_colour):


        settings_window = Toplevel(screen)
        settings_window.title("Settings")
        settings_window.geometry("900x500")

        settings_window.focus_force()
        settings_window.grab_set()

        settings_window.configure(bg=self.main_colour)
        self.change_title_bar(settings_window, self.border_colour)

        list_of_styles = ["Red","Blue","Green"]
        title_label = ttk.Label(settings_window,text = "SETTINGS")

        label = ttk.Label(settings_window,text = "Pick a theme")
        title_label.grid(column = 0,row = 0)
        label.grid(column = 0,row = 1)

        style_choice_buttons = []
        index = 0
        for style in list_of_styles:
            print(style)
            button = ttk.Button(settings_window,text = style,command = lambda current_style=style: self.change_style(global_style,current_style,screen,settings_window,border_colour))
            style_choice_buttons.append(button)
            index += 1

        count = 2
        for button1 in style_choice_buttons:
            button1.grid(column = 0,row = count)
            count +=1

    def change_style(self,style,theme,main_screen, settings_window,border_colour):
        s = ttk.Style()



        if theme == 'Green':
            darker_colour = '#477a42'
            lighter_colour = '#00821e'
            darkest_colour = '#00751b'
            self.border_colour = 0x00125100

        if theme == 'Red':
            darker_colour = '#804242'
            lighter_colour =  '#820000'
            darkest_colour = '#750000'
            self.border_colour = 0x00000051

        if theme == 'Blue':
            lighter_colour = '#34495e'
            darker_colour = '#29445f'
            darkest_colour = '#2c3e50'
            self.border_colour = 0x00372716

        self.main_colour = lighter_colour
        self.change_title_bar(main_screen, self.border_colour)
        self.change_title_bar(settings_window, self.border_colour)

        print(hex(self.border_colour))

        border_colour = self.border_colour

        main_screen.configure(bg=darkest_colour)
        settings_window.configure(bg=self.main_colour)

        s.configure('Blue.TFrame', background=lighter_colour)
        s.configure('Dark_blue.TFrame', background=darker_colour)
        s.configure('Darkest_Blue.TFrame', background = darkest_colour)
        style.configure(
            "Title.TLabel",
            font=("Arial", 32, "bold"),
            foreground="#ecf0f1",
            background= darkest_colour
        )
        style.configure(
            "TLabel",
            font=("Arial", 18, "bold"),
            foreground="#ecf0f1",
            background= lighter_colour
        )
        style.configure(
            "TButton",
            font=("Arial", 12),
            padding=(15, 10),
        )
        style.configure(
            "Left.TFrame",
            background=lighter_colour
        )
        style.configure(
            "Right.TFrame",
            background=darker_colour
        )


    @staticmethod
    def change_title_bar(self,hex_value):

        self.update()

        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        hwnd = ct.windll.user32.GetParent(self.winfo_id())
        rendering_policy = 35
        value = hex_value
        value = ct.c_int(value)

        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
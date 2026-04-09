from Button_menus import *
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Database.database import init_db, add_expense, get_all_expenses, table_monthly_creation
from Calendar import CalendarView



class App(Tk):
    def __init__(self):
        super().__init__()
        self.main_colour = "#34495e"

        self.style = ttk.Style()
        self.setup_styles()

        self.title("Expense-tracker")
        self.is_fullscreen = True
        self.attributes('-fullscreen', True)
        self.configure(bg="#2c3e50")

        self.expenses = []

        self.create_layout()

        init_db()
        self.load_expenses()

        self.bind("<Escape>", self.toggle_fullscreen)
        self.button_menus = Menu()
        self.button_menus.calendar_view = self.calendar_view
        self.border_colour = 0x00372716
        self.button_menus.change_title_bar(self,self.border_colour)

        # profile calls
        # self.profile_all()

        # self.profile_ui_functions()
        # self.profile_all_timed()

    def change_colours(self):
        if self.button_menus.main_colour == '#00821e':
            self.main_colour = '#00821e'
            self.border_colour = 0x00125100

        if self.button_menus.main_colour == '#820000':
            self.main_colour =  '#820000'
            self.border_colour = 0x00000051

        if self.button_menus.main_colour == '#34495e':
            self.main_colour = '#34495e'
            self.border_colour = 0x00372716


    def load_expenses(self):
        rows = get_all_expenses()
        self.expenses = [
            {
                "id": row[0],
                "amount": row[1],
                "category": row[2],
                "date": row[3],
                "note": row[4]
            }
            for row in rows
        ]

    def load_monthly(self):
        self.monthly_expenses =  table_monthly_creation()



    def Monthy_expenses_helper(self):
        self.load_monthly()
        self.button_menus.create_monthly_expenses_window(self.monthly_expenses, self)

    def View_expenses_helper(self):
        self.load_expenses()
        self.button_menus.create_view_expenses_window(self.expenses,self)

    def toggle_fullscreen(self, event=None):
        self.change_colours()
        self.is_fullscreen = not self.is_fullscreen
        self.attributes('-fullscreen', self.is_fullscreen)
        if not self.is_fullscreen:
            self.geometry("1920x1000")
        self.button_menus.change_title_bar(self, self.border_colour)
        print(self.main_colour)
    def setup_styles(self):
        self.style.theme_use('clam')
        s = ttk.Style()

        s.configure('Blue.TFrame', background='#34495e')
        s.configure('Dark_blue.TFrame', background="#29445f")
        s.configure('Darkest_Blue.TFrame', background = '#2c3e50')



        self.style.configure(
            "Title.TLabel",
            font=("Arial", 32, "bold"),
            foreground="#ecf0f1",
            background="#2c3e50"
        )
        self.style.configure(
            "TLabel",
            font=("Arial", 18, "bold"),
            foreground="#ecf0f1",
            background="#34495e"
        )
        self.style.configure(
            "TButton",
            font=("Arial", 12),
            padding=(15, 10),
        )
        self.style.configure(
            "Left.TFrame",
            background="#2c3e50"
        )
        self.style.configure(
            "Right.TFrame",
            background="#34495e"
        )

    def create_layout(self):
        self.title_label = ttk.Label(self, text="EXPENSE TRACKER", style="Title.TLabel")
        self.title_label.grid(row=0, pady=(30, 20))

        self.container = Frame(self, bg="#2c3e50")
        self.container.grid(row=1, padx=50, pady=(0, 30), sticky="nsew")
        
        self.container.columnconfigure(0, weight=0, minsize=700)   
        self.container.columnconfigure(1, weight=1)   
        self.container.rowconfigure(0, weight=1)

        self.create_left_frame()
        self.create_right_frame()
        
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def create_left_frame(self):
        self.left_frame = ttk.Frame(self.container, width=700, height=900,style = 'Blue.TFrame')
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 15))
        self.left_frame.grid_propagate(False)

        self.add_expense_btn = ttk.Button(
            self.left_frame,
            text="+ Add Expense",
            command=lambda: self.button_menus.create_add_expenses_window(self.expenses,self)
        )
        self.add_expense_btn.grid(row=0, column=0, sticky="nw", pady=(30, 10), padx=30)

        self.view_expenses_btn = ttk.Button(self.left_frame, text="View Expenses", command=self.View_expenses_helper)
        self.view_expenses_btn.grid(row=1, column=0, sticky="nw", pady=10, padx=30)

        self.view_summary_btn = ttk.Button(self.left_frame, text="Monthly Summary", command=self.Monthy_expenses_helper)
        self.view_summary_btn.grid(row=2, column=0, sticky="nw", pady=10, padx=30)

        self.settings_button = ttk.Button(self.left_frame, text="Settings", command=lambda: self.button_menus.show_settings_window(self, self.style, self.border_colour))
        self.settings_button.grid(row=3, column=0, sticky="nw", pady=10, padx=30)

        self.exit_btn = ttk.Button(self.left_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row=4, column=0, sticky="nw", pady=(30, 10), padx=30)

    def create_right_frame(self):
    
        self.right_frame = Frame(self.container, bg="#29445f")
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self.calendar_view = CalendarView(self.right_frame)
        self.calendar_view.pack(fill=BOTH, expand=True, padx=20, pady=20)


    def run(self):
        self.mainloop()

   
    
if __name__ == "__main__":
    app = App()
    app.run()
    

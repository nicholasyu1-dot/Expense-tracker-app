from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense-tracker")
        self.is_fullscreen = True
        self.attributes('-fullscreen', True)
        self.configure(bg="#2c3e50")
        
        self.setup_styles()
        self.create_layout()
        
        self.bind("<Escape>", self.toggle_fullscreen)


    def show_add_expenses_window(self):
        self.amount.grid(row = 0,column = 0,padx = 20,pady = 20,ipadx=10,ipady=10)
        self.date.grid(column = 0,row = 1,padx = 20,pady = 20)
        self.type_of_expense.grid(column = 0,row = 2,padx = 20,pady = 20)
        self.amount_entry.grid(column = 1,row = 0,padx = 20,pady = 20)
        self.date_button.grid(column = 1,row = 1,padx = 20,pady = 20)
        self.type_dropdown.grid(column = 1,row = 2,padx = 20,pady = 20)


    def setup_add_expenses_window(self):
        self.add_expenses_window = Toplevel(self)
        self.add_expenses_window.title("Add an expense")
        self.add_expenses_window.geometry(f"1000x700+{self.winfo_screenwidth() // 2 - 1000 // 2}+{self.winfo_screenheight()//2 - 700//2}")
        self.add_expenses_window.focus_force()
        self.add_expenses_window.grab_set()
        self.add_expenses_window.configure(bg = "#34495e")

        self.amount_value = Variable()
        self.amount  = ttk.Label(self.add_expenses_window,text = "Amount spent")
        self.amount.config()
        self.date = ttk.Label(self.add_expenses_window,text = "Select a date")
        self.type_of_expense = ttk.Label(self.add_expenses_window,text = "Select a type")
        self.amount_entry = ttk.Entry(self.add_expenses_window,textvariable = self.amount_value)
        self.date_button  = ttk.Button(self.add_expenses_window,text = "Choose a date")
        self.selected_type = StringVar()
        self.options = ["select an option","Food","Clothing","Medicine","video games","Custom"]
        self.type_dropdown = ttk.OptionMenu(self.add_expenses_window,self.selected_type,*self.options)


    def create_add_expenses_window(self):
        self.setup_add_expenses_window()
        self.show_add_expenses_window()


    def toggle_fullscreen(self, event = None):
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
            "Heading.TLabel",
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
        self.title_label.pack(pady=(30, 20))  
        
        self.container = Frame(self, bg="#2c3e50")
        self.container.pack(fill=BOTH, expand=True, padx=50, pady=(0, 30))  
        
      
        self.left_frame = Frame(self.container, bg="#3a546e")
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True)  
        
        self.add_expense_btn = ttk.Button(self.left_frame, text="+ Add Expense")
        self.add_expense_btn.pack(anchor="w", pady=10)  
        
        self.view_expenses_btn = ttk.Button(self.left_frame, text="View Expenses")
        self.view_expenses_btn.pack(anchor="w", pady=10)  
        
        self.view_summary_btn = ttk.Button(self.left_frame, text="Monthly Summary")
        self.view_summary_btn.pack(anchor="w", pady=10)
        
        self.settings_button = ttk.Button(self.left_frame, text="Settings")
        self.settings_button.pack(anchor="w", pady=10)
        
        self.exit_btn = ttk.Button(self.left_frame, text="Exit", command=self.quit)
        self.exit_btn.pack(anchor="w", pady=(30, 10)) 
        
       
        self.right_frame = Frame(self.container, bg="#29445f", width=1200)  
        self.right_frame.pack(side=RIGHT, fill=Y, padx=(0, 0))  
        self.right_frame.pack_propagate(False)  
        
        self.calendar_label = ttk.Label(
            self.right_frame, 
            text="CALENDAR", 
            style="Heading.TLabel"
        )
        self.calendar_label.pack(pady=20)
        
        self.calendar_placeholder = Label(
            self.right_frame,
            text="Calendar is here",
            font=("Arial", 12),
            fg="#7f8c8d",
            bg="#34495e"
        )
        self.calendar_placeholder.pack(expand=True)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

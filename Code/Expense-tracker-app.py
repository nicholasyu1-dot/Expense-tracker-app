import tkinter
from cProfile import label
from tkinter import *
from tkinter import ttk

from pywin.dialogs.ideoptions import buttonControlMap


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

    def add_expenses(self):
        add_expenses_window = Toplevel(self)
        add_expenses_window.title("Add an expense")
        add_expenses_window.geometry(f"1000x700+{self.winfo_screenwidth() // 2 - 1000 // 2}+{self.winfo_screenheight()//2 - 700//2}")
        add_expenses_window.focus_force()
        add_expenses_window.grab_set()
        amount_value = Variable()
        Amount  = ttk.Label(add_expenses_window,text = "Amount spent/")
        date = ttk.Label(add_expenses_window,text = "Select a date")

        type_of_expense = ttk.Label(add_expenses_window,text = "Select a type")
        Amount_entry = ttk.Entry(add_expenses_window,textvariable=amount_value)
        date_button  = ttk.Button(add_expenses_window,text = "Choose a date")
        Selected_type = StringVar()
        options = ["select an option","Food","Clothing","Medicine","video games","Custom"]
        Type_dropdown = ttk.OptionMenu(add_expenses_window,Selected_type,*options)
        Amount.grid(row = 0,column = 0,padx = 20,pady = 20)
        date.grid(column = 0,row = 1,padx = 20,pady = 20)
        type_of_expense.grid(column = 0,row = 2,padx = 20,pady = 20)
        Amount_entry.grid(column = 1,row = 0,padx = 20,pady = 20)
        date_button.grid(column = 1,row = 1,padx = 20,pady = 20)
        Type_dropdown.grid(column = 1,row = 2,padx = 20,pady = 20)

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
        self.title_label.grid(pady=(30, 20))
        
        self.container = Frame(self, bg="#2c3e50")
        self.container.columnconfigure(0,weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(5,weight=1)
        self.container.rowconfigure(5, weight=1)
        self.container.grid(padx=50, pady=(0, 30))

      
        self.left_frame = Frame(self.container, bg="#3a546f",width=800,height=500)
        self.left_frame.columnconfigure(0,weight=1)
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.grid(row = 0,column = 0,columnspan=4,padx = (0,0),sticky="nsew")
        self.left_frame.grid_propagate(False)
        
        self.add_expense_btn = ttk.Button(self.left_frame, text="+ Add Expense",command = self.add_expenses)
        self.add_expense_btn.grid(row = 0,column = 0,sticky="nw", pady=10)
        
        self.view_expenses_btn = ttk.Button(self.left_frame, text="View Expenses")
        self.view_expenses_btn.grid(row = 1,column = 0,sticky="w", pady=10)
        
        self.view_summary_btn = ttk.Button(self.left_frame, text="Monthly Summary")
        self.view_summary_btn.grid(row = 2,column = 0,sticky="nw", pady=10)
        
        self.settings_button = ttk.Button(self.left_frame, text="Settings")
        self.settings_button.grid(row = 3,column = 0,sticky="nw", pady=10)
        
        self.exit_btn = ttk.Button(self.left_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row = 4,column = 0,sticky="nw", pady=(30, 10))
        
       
        self.right_frame = Frame(self.container, bg="#29445f", width=1200)
        self.right_frame.grid(row = 0,column = 5,padx=(0, 0),rowspan=10,sticky = "nsew")
        self.right_frame.grid_propagate(False)
        
        self.calendar_label = ttk.Label(
            self.right_frame, 
            text="CALENDAR", 
            style="Heading.TLabel"
        )
        self.calendar_label.grid(row = 0,column = 1,pady=20)
        
        self.calendar_placeholder = Label(
            self.right_frame,
            text="Calendar is here",
            font=("Arial", 12),
            fg="#7f8c8d",
            bg="#34495e"
        )
        self.calendar_placeholder.grid(row = 1,column = 5,columnspan=5)
       #  self.helper_frame = Frame(self.container,width = 1,)

        he1 = ""
        he2= ""
        he3= ""
        he4= ""
        he5= ""
        he6= ""
        he7= ""
        he8= ""
        helpers = [he1,he2,he3,he4,he5,he6,he7,he8]
        row = 1
        column = 1
        # for helper in helpers:
        #     helper = Frame(self.container,width = 300,height=100,borderwidth=0,border=0)
        #     helper.grid(column=column,row = row)
        #     column +=1
        #     row +=1

        #self.helper_frame.grid(column = 1000,row = 1000,sticky = "nsew")
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
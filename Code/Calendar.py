from tkinter import *
from datetime import datetime, timedelta
from collections import defaultdict

class InteractiveCalendar(Frame):
    def __init__(self, parent, expenses=None, callback=None):
        super().__init__(parent)
        self.parent = parent
        self.expenses = expenses or []
        self.callback = callback
        self.current_date = datetime.now()
        
        self.expenses_by_date = self._build_expense_map()
        self.create_calendar_ui()
    
    def _build_expense_map(self):
        expense_map = defaultdict(list)
        for expense in self.expenses:
            expense_map[expense["date"]].append(expense)
        return expense_map
    
    def create_calendar_ui(self):
        # Top buttons
        top_frame = Frame(self)
        top_frame.pack()
        
        Button(top_frame, text="Prev", command=self.prev_month, width=10).pack(side=LEFT)
        self.month_label = Label(top_frame, text=self.current_date.strftime("%B %Y"), font=("Arial", 14))
        self.month_label.pack(side=LEFT, padx=20)
        Button(top_frame, text="Next", command=self.next_month, width=10).pack(side=LEFT)
        
        # Days header
        days_frame = Frame(self)
        days_frame.pack()
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            Label(days_frame, text=day, width=15, relief=RIDGE, borderwidth=1).pack(side=LEFT)
        
        # Calendar grid
        self.calendar_frame = Frame(self)
        self.calendar_frame.pack(fill=BOTH, expand=True)
        
        self.draw_calendar()
    
    def draw_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        year = self.current_date.year
        month = self.current_date.month
        
        first_day = datetime(year, month, 1)
        first_weekday = first_day.weekday()
        
        if month == 12:
            last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = datetime(year, month + 1, 1) - timedelta(days=1)
        
        num_days = last_day.day
        
        day_num = 1
        for week in range(6):
            for day_of_week in range(7):
                if week == 0 and day_of_week < first_weekday:
                    Label(self.calendar_frame, text="", relief=RIDGE, borderwidth=1).grid(row=week, column=day_of_week, sticky="nsew")
                elif day_num <= num_days:
                    date_str = f"{year}-{month:02d}-{day_num:02d}"
                    has_expense = date_str in self.expenses_by_date
                    
                    text = str(day_num)
                    if has_expense:
                        text += "\n[*]"
                    
                    btn = Button(
                        self.calendar_frame,
                        text=text,
                        relief=RIDGE,
                        borderwidth=1,
                        command=lambda ds=date_str: self.on_day_click(ds)
                    )
                    btn.grid(row=week, column=day_of_week, sticky="nsew")
                    day_num += 1
                else:
                    Label(self.calendar_frame, text="", relief=RIDGE, borderwidth=1).grid(row=week, column=day_of_week, sticky="nsew")
            
            self.calendar_frame.rowconfigure(week, weight=1)
        
        for col in range(7):
            self.calendar_frame.columnconfigure(col, weight=1)
    
    def on_day_click(self, date_str):
        if self.callback:
            self.callback(date_str)
    
    def prev_month(self):
        if self.current_date.month == 1:
            self.current_date = datetime(self.current_date.year - 1, 12, 1)
        else:
            self.current_date = datetime(self.current_date.year, self.current_date.month - 1, 1)
        
        self.month_label.config(text=self.current_date.strftime("%B %Y"))
        self.draw_calendar()
    
    def next_month(self):
        if self.current_date.month == 12:
            self.current_date = datetime(self.current_date.year + 1, 1, 1)
        else:
            self.current_date = datetime(self.current_date.year, self.current_date.month + 1, 1)
        
        self.month_label.config(text=self.current_date.strftime("%B %Y"))
        self.draw_calendar()
    
    def update_expenses(self, expenses):
        self.expenses = expenses
        self.expenses_by_date = self._build_expense_map()
        self.draw_calendar()
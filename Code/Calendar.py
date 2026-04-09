from tkinter import Frame, Label, Button, Text, END
import calendar
from datetime import datetime
import os
import sys
from tkinter import ttk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Database.database import get_expenses_by_date


class CalendarView(Frame):



    def __init__(self, parent):
        super().__init__(parent, bg="#29445f")
        self.configure(bg="#29445f")

        today = datetime.today()
        self.current_year = today.year
        self.current_month = today.month

        self.create_widgets()
        self.build_calendar()

    def create_widgets(self):
        self.header_frame = ttk.Frame(self, style = "Dark_blue.TFrame")
        self.header_frame.pack(fill="x", pady=20)

        self.prev_button = ttk.Button(
            self.header_frame,
            text="<",

            width=4,
            command=self.previous_month
        )
        self.prev_button.pack(side="left", padx=(140, 10))

        self.month_label = ttk.Label(
            self.header_frame,
            text="",
            font=("Arial", 20, "bold"),

        )
        self.month_label.pack(side="left", padx=20)

        self.next_button = ttk.Button(
            self.header_frame,
            text=">",

            width=4,
            command=self.next_month
        )
        self.next_button.pack(side="left", padx=10)

        self.calendar_frame = Frame(self, bg="#29445f")
        self.calendar_frame.pack(fill="x", padx=20, pady=10)

        self.selected_date_label = ttk.Label(
            self,
            text="Select a date",
            font=("Arial", 16, "bold"),

        )
        self.selected_date_label.pack(pady=(25, 10))

        self.expense_display = Text(
            self,
            height=12,
            font=("Arial", 12),
            bg="#3a546f",
            fg="white",
            relief="flat",
            bd=0,
            insertbackground="white"
        )
        self.expense_display.pack(fill="x", padx=60, pady=10)
        self.expense_display.insert(END, "No date selected yet.")
        self.expense_display.config(state="disabled")

        self.total_label = ttk.Label(
            self,
            text="Total: 0",
            font=("Arial", 14, "bold"),

        )
        self.total_label.pack(pady=10)

    def build_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        for col in range(7):
            self.calendar_frame.grid_columnconfigure(col, weight=1)

        self.month_label.config(
            text=f"{calendar.month_name[self.current_month]} {self.current_year}"
        )

        day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day_name in enumerate(day_names):
            lbl = Label(
                self.calendar_frame,
                text=day_name,
                font=("Arial", 11, "bold"),
                bg="#29445f",
                fg="#bdc3c7",
                pady=8
            )
            lbl.grid(row=0, column=col, padx=4, pady=4, sticky="nsew")

        weeks = calendar.monthcalendar(self.current_year, self.current_month)

        for row_index, week in enumerate(weeks, start=1):
            self.calendar_frame.grid_rowconfigure(row_index, weight=1)

            for col_index, day in enumerate(week):
                if day == 0:
                    empty = Label(
                        self.calendar_frame,
                        text="",
                        bg="#29445f",
                        height=3
                    )
                    empty.grid(row=row_index, column=col_index, padx=4, pady=4, sticky="nsew")
                else:
                    btn = Button(
                        self.calendar_frame,
                        text=str(day),
                        font=("Arial", 11, "bold"),
                        bg="#3a546f",
                        fg="white",
                        activebackground="#5d7b99",
                        activeforeground="white",
                        relief="flat",
                        height=3,
                        command=lambda d=day: self.show_expenses_for_date(d)
                    )
                    btn.grid(row=row_index, column=col_index, padx=4, pady=4, sticky="nsew")

    def show_expenses_for_date(self, day):
        selected_date = f"{self.current_year:04d}-{self.current_month:02d}-{day:02d}"
        expenses = get_expenses_by_date(selected_date)

        self.selected_date_label.config(text=f"Expenses for {selected_date}")

        self.expense_display.config(state="normal")
        self.expense_display.delete("1.0", END)

        total = 0

        if not expenses:
            self.expense_display.insert(END, "No expenses for this day.")
        else:
            for _, amount, category, date, note in expenses:
                self.expense_display.insert(
                    END,
                    f"Amount: {amount}\nCategory: {category}\nNote: {note}\n\n"
                )
                total += amount

        self.expense_display.config(state="disabled")
        self.total_label.config(text=f"Total: {total}")

    def previous_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.build_calendar()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.build_calendar()

    def change_colour_cal(self, darkest_colour,lighter_colour, darker_colour):


        self.style = ttk.Style()

        self.style.configure(
            "Title.TLabel",
            font=("Arial", 32, "bold"),
            foreground="#ecf0f1",
            background= darkest_colour
        )
        self.style.configure(
            "TLabel",
            font=("Arial", 18, "bold"),
            foreground="#ecf0f1",
            background= lighter_colour
        )
        self.style.configure(
            "TButton",
            font=("Arial", 12,'bold'),
            padding=(15, 10),
            foreground="white",
            background= 'blue'

        )
        self.style.map('TButton', background=[('active', 'blue')])

        self.style.configure(
            "Left.TFrame",
            background=lighter_colour
        )
        self.style.configure(
            "Right.TFrame",
            background=darker_colour
        )
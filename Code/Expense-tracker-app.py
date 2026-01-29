from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.create_main_menu_and_show()


    def create_main_menu_and_show(self):
        self.geometry(f"{self.winfo_screenwidth()}+{self.winfo_screenheight()}")
        label = ttk.Label(self, width = width, text = text,justify= alignment, anchor = anchor)
        label.config(font=(font, size))



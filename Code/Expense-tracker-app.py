from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.create_main_menu()
        self.title("Expense-tracker")
        self.attributes('-fullscreen',True)
        self.setup_buttons()
        self.show_main_menu()


    def create_main_menu(self):
        self.Main_menu_title = ttk.Label(self, text = "MAIN MENU")
        self.Main_menu_title.config(font=("Arial", 30))


    def setup_buttons(self):
        self.settings_button = ttk.Button(self, text = "Settings",command = self.settings_menu)

    def settings_menu(self):
        self.hide_main_menu()
        self.settings_title = ttk.Label(self, text = "SETTINGS")
        self.settings_title.config(font = ("Arial",60))
        self.Setting_1 = self.create_label( text = "Setting_1")
        self.Setting_2 = self.create_label( text = "Setting_2")
        self.Setting_3 = self.create_label( text = "Setting_3")
        self.Setting_4 = self.create_label( text = "Setting_4")
        self.Setting_5 = self.create_label( text = "Setting_5")

        self.Setting_1.grid(row=1,column = 0)
        self.Setting_2.grid(row=2,column = 0)
        self.Setting_3.grid(row=3,column = 0)
        self.Setting_4.grid(row=4,column = 0)
        self.Setting_5.grid(row=5,column = 0)
        self.settings_title.grid(row = 0,column=0,pady=1)



        self.back_button = ttk.Button(self, text = "back",command = self.hide_settings)
        self.back_button.grid(sticky="W",padx=(self.winfo_screenwidth()/2-105),row=6,column=0)

    def hide_main_menu(self):
        self.Main_menu_title.grid_remove()
        self.settings_button.grid_remove()

    def show_main_menu(self):
        self.Main_menu_title.grid(sticky="W",padx=(self.winfo_screenwidth()/2-105),row=0,column=0)
        self.settings_button.grid(sticky="W",padx=(self.winfo_screenwidth()/2-105),row=1,column=0)

    def create_label(self,text,font = "Arial",size = 30):
        label = ttk.Label(self, text=text)
        label.config(font = (font,size))
        return label

    def run(self):
        self.mainloop()

    def hide_settings(self):
        self.Setting_1.grid_remove()
        self.Setting_2.grid_remove()
        self.Setting_3.grid_remove()
        self.Setting_4.grid_remove()
        self.Setting_5.grid_remove()
        self.settings_title.grid_remove()
        self.back_button.grid_remove()
        self.show_main_menu()



if __name__ == "__main__":
    app = App()
    app.run()
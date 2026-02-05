from sqlite3 import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class App(Tk):
    def __init__(self):
        super().__init__()
        self.create_main_menu()
        self.title("Expense-tracker")
        self.attributes('-fullscreen',True)
        self.setup_buttons()
        self.show_main_menu()
        self.file_title = ""

        self.setup_table()
        self.table.grid()


    def setup_table(self, show="tree", height=10):
        self.table =  ttk.Treeview(self, show=show, height=height)

    def add_to_table(self, table, values):
        data = []
        for arg in values:
            data.append(arg)

        table.insert('', 'end', values=data)

    def add_table_columns_and_display(self, table, *args):
        column = []

        for arg in args:
            column += arg,
        table['columns'] = column
        count = 0

        for arg in args:
            if count >= 0:
                table.heading(count, text=arg)
                table.column(count, minwidth=2, stretch=True)
            count += 1


    def create_main_menu(self):
        self.Main_menu_title = ttk.Label(self, text = "MAIN MENU")
        self.Main_menu_title.config(font=("Arial", 30))


    def new_table(self):
        self.new_label = ttk.Label(self, text = "NEW file")
        file_name = ""

        filename = filedialog.askopenfilename()
        print(filename)
        if filename != "":
            opened_file = open(filename)
            #self.text_box.delete(1.0, END)
            #if not self.save_state:
                #self.saveFile()
            #for line in opened_file:
                #self.text_box.insert(END, line)
            opened_file.close()

    def saveFile(self):
        file_types = [ ("Text documents", "*.txt"),
                       ("All files", "*.*")]

        filename = filedialog.asksaveasfilename(filetypes=file_types,initialfile=self.file_title)
        if filename != "":
            file = open(filename, mode='w')
            #file.write(data)
            file.close()
        self.filename = str(filename.split("/")[-1:][0])
        self.title(self.filename)
        print(type(filename))

        self.save_state = True
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
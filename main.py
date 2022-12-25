import tkinter as tk
from tkinter import ttk
# from menu import menu1_open
from backend import geometry_param, menu_options
# from menu2 import menu2_open
# from menu3 import menu3_open


# window_main = Tk()
#
# window_main.geometry(geometry_param)
# window_main.title("Main Menu")


# btn_pract_1 = Button(window_main, text=menu_options[0], command=menu1_open)
# btn_pract_1.grid(row=0, column=0, sticky="nsew")
#
# btn_pract_2 = Button(window_main, text=menu_options[1], command=menu2_open)
# btn_pract_2.grid(row=1, column=0, sticky="nsew")
#
# btn_pract_3 = Button(window_main, text=menu_options[2], command=menu3_open)
# btn_pract_3.grid(row=2, column=0, sticky="nsew")
# settings = Button(window_main, text=menu_options[3], command=lambda :raise_window(kek()))
# settings.grid(row=3, column=0, sticky="nsew")

# window_main.mainloop()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Settings')

        self.create_widgets()

    def create_widgets(self):
        btn_pract_1 = tk.Button(self, text=menu_options[0], width=18, relief='groove', background='#e1e1e1')
        btn_pract_1.place(relx=0.5, rely=0.3, anchor='center')
        # btn_pract_1.grid(row=0, column=0, sticky="ns", padx=70)

        btn_pract_2 = tk.Button(self, text=menu_options[1], width=18, relief='groove', background='#e1e1e1')
        btn_pract_2.place(relx=0.5, rely=0.42, anchor='center')
        # btn_pract_2.grid(row=1, column=0, sticky="ns", padx=70)
        #
        btn_pract_3 = tk.Button(self, text=menu_options[2], width=18, relief='groove', background='#e1e1e1')
        btn_pract_3.place(relx=0.5, rely=0.54, anchor='center')
        # btn_pract_3.grid(row=2, column=0, sticky="ns", padx=70)

        menubar = tk.Menu(self)
        self.config(menu=menubar, pady=100, bg='pink')
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='Settings', menu=file_menu)
        sub_menu = tk.Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='960x480', command=lambda: self.geometry('960x480'))
        sub_menu.add_command(label='1156x756', command=lambda: self.geometry('1156x756'))
        sub_menu.add_command(label='1920x1080', command=lambda: self.geometry('1920x1080'))
        file_menu.add_cascade(label='Screen resolution', menu=sub_menu)


main_window = MainWindow()
main_window.mainloop()

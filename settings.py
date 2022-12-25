import tkinter as tk
from tkinter import ttk
from backend import geometry_param

# def settings_open():
#     window_settings = Toplevel()
#     window_settings.geometry(geometry_param)
#     window_settings.title('Settings')
#
#
#     window_settings.mainloop()

window = tk.Tk()
window.geometry('400x400')

frame1=tk.Frame(window)
frame2=tk.Frame(window)


def change_to_frame2():
    frame2.pack()
    frame1.forget()


def change_to_frame1():
    frame1.pack()
    frame2.forget()

btn1 = tk.Button(window, text='switch to frame 2', command=change_to_frame2)
btn1.pack()

lbl1 = tk.Label(frame1, text='frame1')
lbl1.pack()

btn2 = tk.Button(window, text='switch back to frame 1', command=change_to_frame1)
btn2.pack()

lbl2 = tk.Label(frame2, text='frame2')
lbl2.pack()

window.mainloop()

from tkinter import *
from backend import geometry_param

# def settings_open():
#     window_settings = Toplevel()
#     window_settings.geometry(geometry_param)
#     window_settings.title('Settings')
#
#
#     window_settings.mainloop()

window = Tk()
window.geometry('1363x692')

lbl = Label(window, text='00:00:00', font=('Arial', '30'))
lbl.pack()

status = False
seconds, minutes, hours = 0, 0, 0


def start_count():
    global status
    if not status:
        update()
        status = True


def update():
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_str = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_str = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_str = f'{seconds}' if seconds > 9 else f'0{seconds}'
    lbl.config(text=f'{hours_str}:{minutes_str}:{seconds_str}')
    global update_time
    update_time = lbl.after(1000, update)


def stop_count():
    global status
    if status:
        lbl.after_cancel(update_time)
        status = False


btn = Button(window, text='start', command=start_count)
btn.pack()

btn_stop = Button(window, text='stop', command=stop_count)
btn_stop.pack()

def new_watchcount():
    obj = WindowClass(window)

btn_new = Button(window, text='new watchcount', command=new_watchcount)
btn_new.pack()


class WindowClass:
    def __init__(self, master):
        self.master = master


window.mainloop()

# import unittest
# import menu
#
# '''
# What menu is capable of:
#
# '''
# class TestMenu(unittest.TestCase):

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1600x1200')

frame0 = Frame(root)
frame0.grid(row=1, column=0, sticky=W)

frame1 = Frame(root, bg='green')
frame1.grid(row=1, column=0, sticky=NS)

frame2 = Frame(root)
frame2.grid(row=2, column=0, sticky=NS)

frame3 = Frame(root)
frame3.grid(row=1, column=0, sticky=E)

# frameN = Frame(root)
# frameN.grid(row=3, column=0, sticky=NS)

lbl_suggested = ttk.Label(root, text="Press 'Get kanji' to start", width=20, font=('Arial', 50))
lbl_suggested.configure(anchor='center')
lbl_suggested.grid(row=0, column=0, sticky="we", ipady=50, ipadx=50)



lbl_hist = ttk.Label(frame0, text="History:")
lbl_hist.grid(row=0, column=0)

list_history = Text(frame0, width=15)
list_history.grid(row=1, column=0)

lbl_reply = ttk.Label(frame1, text="")
lbl_reply.grid(row=0, column=0)

lbl_reply = ttk.Label(frame1, text="Answer:")
lbl_reply.grid(row=1, column=0, sticky=W)

ent_answer = ttk.Entry(frame1, font=50)
ent_answer.grid(row=1, column=0, sticky=E)

lbl_score = ttk.Label(frame1, text="Score")
lbl_score.configure(anchor='center')
lbl_score.grid(row=2, column=0)

btn_submit = ttk.Button(frame1, text="Submit")
btn_submit.grid(row=2, column=1)

btn_rand_kanji = ttk.Button(frame1, text="Get kanji")
btn_rand_kanji.grid(row=1, column=2)

btn_curr_check = ttk.Button(frame1, text="Search: Current kanji")
btn_curr_check.grid(row=2, column=2)


# lbl_jlpt_from = ttk.Label(frame2, text="JLPT level from:")
# lbl_jlpt_from.grid(row=6, column=0)
#
# ent_jlpt_from = ttk.Entry(frame2, font=50)
# ent_jlpt_from.grid(row=6, column=0)
# ent_jlpt_from.focus()
#
# lbl_jlpt_to = ttk.Label(frame2, text="to:")
# lbl_jlpt_to.grid(row=7, column=0, sticky="w")
#
# ent_jlpt_to = ttk.Entry(frame2, font=50)
# ent_jlpt_to.grid(row=7, column=0)
#
# btn_submit_jlpt = ttk.Button(frame2, text="Submit")
# btn_submit_jlpt.grid(row=8, column=0)
#
#
#

# lbl_log = ttk.Label(frame3, text="Updates:")
# lbl_log.grid(row=0, column=0, padx=200)
#
# list_log = Text(frame3)
# list_log.grid(row=1, column=0, padx=200)





# btn_submit = Button(root, text="Submit", width=30, font=('Arial', 50))
# btn_submit.configure(anchor='center')
# btn_submit.grid(row=0, column=0)
#
# btn_submit2 = Button(frame2, text="frame2", width=30)
# btn_submit2.grid(row=0, column=0)
#
# btn_submit3 = Button(frame3, text="frame3", width=50)
# btn_submit3.grid(row=0, column=0)
#
# btn_submit1 = Button(frame1, text="frame1", width=30)
# btn_submit1.grid(row=1, column=1)
#
# btn_submit0 = Button(frame0, text="frame0", width=50)
# btn_submit0.grid(row=0, column=0)
#
# btn_submitN = Button(frameN, text="frameN", width=30)
# btn_submitN.grid(row=0, column=0)

root.mainloop()
from tkinter import *
from tkinter import messagebox, ttk
import webbrowser
import backend
from achievements import get_achievement, score_related_achievements

checker_storage = ""
score = 0
url = "https://jisho.org/search/"


# def menu1_open():
window = Tk()
window.geometry('1400x789')
window.title(backend.menu_options[0])


def log_kanji():
    logger = backend.logger_file()
    list_log.delete('1.0', 'end')
    list_log.insert(END, logger)


def check_achievements(answer):
    get_achievement(answer)
    total_score_for_achievement_count = backend.total_score_open_file()
    backend.total_score_add(total_score_for_achievement_count)
    score_related_achievements(backend.total_score_open_file())


def jlpt_level():
    j_from = ent_jlpt_from.get()
    j_to = ent_jlpt_to.get()
    return backend.get_jlpt_lvl(j_from, j_to)


def random_kanji():
    global checker_storage
    lbl_suggested['text'] = backend.random_kanji()
    checker_storage = lbl_suggested['text']


def checker():
    global checker_storage

    temp_answer = ent_answer.get()

    def jisho_check():
        global score
        if checker_storage in temp_answer and temp_answer == api_word:
            score += 1
            lbl_score["text"] = score
            # insert random kanji + reply into the text box
            list_history.insert(END, f"{checker_storage} -> {temp_answer}\n")
            check_achievements(temp_answer)
            random_kanji()
        elif checker_storage not in temp_answer or temp_answer != api_word:
            score -= 1
            lbl_score["text"] = score
            list_history.insert(END, f"Provided answer {temp_answer} doesn't contain this kanji {checker_storage}\n")

    if not backend.error_handler(temp_answer):
        log_kanji()
    else:
        if backend.symbol_check(temp_answer):
            response = backend.json_request(temp_answer)
            if not backend.length_printable(temp_answer, response):
                log_kanji()
            else:
                api_word = backend.length_printable(temp_answer, response)
                jisho_check()
        elif not backend.symbol_check(temp_answer):
            log_kanji()

    ent_answer.delete(0, END)


# making Search option from popup window
# search for selected text in jisho
def search_tool():
    try:
        selected_text = window.selection_get()
        webbrowser.open_new_tab(url + selected_text)
    except:
        messagebox.showerror("Text not selected", "Please highlight text you want to search for")


# search jisho for the word from the query section
def check_curr():
    webbrowser.open_new_tab(url + checker_storage)


# making popup window
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


frame1 = Frame(window, width=500, height=1000)
frame1.pack()

frame2 = Frame(window, width=10, height=10)
frame2.pack(side='left', anchor=N)

frame3 = Frame(window, width=50, height=100)
frame3.pack(side='left', anchor=N)

frame4 = Frame(window, width=50, height=100)
frame4.pack(side='left', anchor=N)

lbl_hist = ttk.Label(frame2, text="History:")
lbl_hist.grid(row=0, column=0, sticky="w", padx=20)

list_history = Text(frame2, height=32, width=49, font=50)
list_history.grid(row=1, column=0, sticky="sn", padx=20)

# right click on text box will create popup window
list_history.bind("<Button-3>", do_popup)
# popup menu with defined Search option
m = Menu(window, tearoff=0)
m.add_command(label="Search", command=search_tool)

lbl_suggested = ttk.Label(frame1, text="Press 'Get kanji' to start", width=20, font=('Arial', 50))
lbl_suggested.configure(anchor='center')
lbl_suggested.grid(row=0, column=0, sticky="we", ipady=50, ipadx=50)


lbl_hist = ttk.Label(frame2, text="History:")
lbl_hist.grid(row=0, column=0, sticky="w", padx=20)

list_history = Text(frame2, height=32, width=49, font=50)
list_history.grid(row=1, column=0, sticky="sn", padx=20)

lbl_space = ttk.Label(frame3, text='')
lbl_space.grid(row=5, column=0, pady=220)

lbl_jlpt_from = ttk.Label(frame3, text="JLPT level from:")
lbl_jlpt_from.grid(row=6, column=0, sticky="w")

ent_jlpt_from = ttk.Entry(frame3, font=50)
ent_jlpt_from.grid(row=7, column=0, sticky="e", padx=100)
ent_jlpt_from.focus()

lbl_jlpt_to = ttk.Label(frame3, text="to:")
lbl_jlpt_to.grid(row=7, column=0, sticky="w")

ent_jlpt_to = ttk.Entry(frame3, font=50)
ent_jlpt_to.grid(row=6, column=0)

btn_submit_jlpt = ttk.Button(frame3, text="Submit", width=30, command=jlpt_level)
btn_submit_jlpt.grid(row=8, column=0)

lbl_jlpt_to = ttk.Label(frame3, text="")
lbl_jlpt_to.grid(row=0, column=0, sticky="s")

lbl_reply = ttk.Label(frame3, text="Answer:")
lbl_reply.grid(row=1, column=0, sticky="w")

ent_answer = ttk.Entry(frame3, font=50)
ent_answer.grid(row=1, column=0)

lbl_score = ttk.Label(frame3, text="Score")
lbl_score.configure(anchor='center')
lbl_score.grid(row=2, column=0, sticky="w")

btn_submit = ttk.Button(frame3, text="Submit", width=30, command=checker)
btn_submit.grid(row=2, column=0)

btn_rand_kanji = ttk.Button(frame3, text="Get kanji", width=12, command=random_kanji)
btn_rand_kanji.grid(row=1, column=0, sticky=E)

btn_curr_check = ttk.Button(frame3, text="Lookup kanji", width=12, command=check_curr)
btn_curr_check.grid(row=2, column=0, sticky=E)

lbl_log = ttk.Label(frame4, text="Updates:")
lbl_log.grid(row=0, column=0, sticky="w", padx=20)

list_log = Text(frame4, height=32, width=50, font=50)
list_log.grid(row=1, column=0, sticky="sn", padx=20)

backend.settings(window)

window.mainloop()

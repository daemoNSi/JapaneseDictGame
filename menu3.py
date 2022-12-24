from tkinter import *
from tkinter import messagebox, ttk
import requests
import webbrowser
from backend import menu_options
import re
import backend
from achievements import get_achievement, score_related_achievements

checker_storage = ""
score = 0
url = "https://jisho.org/search/"
translation_list = []
get_all_translations_list = []
translation_list_edit = []


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


# def menu3_open():
window_2 = Tk()
window_2.geometry('1363x692')
window_2.title(menu_options[2])


# Format translations received from get_all_translations
def list_of_translations():
    global translation_list_edit
    for i in get_all_translations_list:
        words = re.sub("[\(\[].*?[\)\]]", '', i)
        translation_list.append(words)
    for k in translation_list:
        translation_list_edit.append(k.lstrip().rstrip().lower())


# Getting all translations from the info received with request to API
def get_all_translations(word):
    global get_all_translations_list
    # english_definitions = get_word.get('senses')
    # for i in english_definitions:
    for i in word.get('senses'):
        iterator = i['english_definitions']
        for k in iterator:
            get_all_translations_list.append(k)

# class shitty_class:
#     def __init__(self, shit, cls_list):
#         self.shit = shit
#         self.cls_list = cls_list
#
#     def check_shit(self, cls_list):
#         for i in get_all_translations_list:
#             words = re.sub("[\(\[].*?[\)\]]", '', i)
#             cls_list.append(words)
#         for k in cls_list:
#             translation_list_edit.append(k.lstrip().rstrip().lower())

# Getting reply from the user, checking its validity, updating score
def checker():
    temp_answer_spelling = ent_answer_spelling.get().lstrip().rstrip()
    temp_answer_translation = ent_answer_translation.get().lstrip().rstrip().lower()

    def jisho_check():
        global score
        response = requests.get("https://jisho.org/api/v1/search/words?keyword=" + checker_storage)
        get_word = response.json()["data"][0]
        jisho_spelling = get_word.get("japanese")[0]["reading"]
        get_all_translations(get_word)
        list_of_translations()
        result = f"{checker_storage} -> {jisho_spelling} / {temp_answer_translation}"
        if temp_answer_spelling == jisho_spelling and temp_answer_translation in translation_list_edit:
            score += 2
            list_history.insert(END, f"\n{checker_storage} -> {jisho_spelling} / {temp_answer_translation}\n")
            check_achievements(checker_storage)
            random_kanji()
        elif temp_answer_spelling != jisho_spelling and temp_answer_translation in translation_list_edit:  # incorrect spelling
            score += 1
            list_history.insert(END, f"\n{checker_storage} -> {temp_answer_spelling} / {temp_answer_translation}. MISTAKE: < {temp_answer_spelling} > is incorrect\n")
            random_kanji()
        elif temp_answer_translation not in translation_list_edit and temp_answer_spelling == jisho_spelling:  # incorrect translation
            score += 1
            list_history.insert(END, f"\n{result}. MISTAKE: < {temp_answer_translation} > is incorrect\n")
            check_achievements(checker_storage)
            random_kanji()
        elif temp_answer_spelling != jisho_spelling or temp_answer_translation not in translation_list_edit:  # both are incorrect
            score -= 2
            list_history.insert(END, f"\n{checker_storage} -> {temp_answer_spelling} / {temp_answer_translation}. MISTAKE: < {temp_answer_spelling} > and < {temp_answer_translation} > are incorrect\n")
        lbl_score["text"] = score
        translation_list_edit.clear()
        translation_list.clear()
        get_all_translations_list.clear()

    if not backend.error_handler(temp_answer_spelling) or not backend.error_handler(temp_answer_spelling):
        log_kanji()
    else:
        if backend.symbol_check(temp_answer_spelling):
            jisho_check()
            ent_answer_spelling.delete(0, END)
            ent_answer_translation.delete(0, END)
        elif not backend.symbol_check(temp_answer_spelling):
            log_kanji()


# making popup window for history
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


# making Search option from popup window
# search for selected text in jisho
def search_tool():
    try:
        selected_text = window_2.selection_get()
        webbrowser.open_new_tab(url + selected_text)
    except:
        messagebox.showerror("Text not selected", "Please highlight text you want to search for")


# search jisho for the word from the query section
def check_curr():
    webbrowser.open_new_tab(url + checker_storage)


frame1 = Frame(window_2, width=500, height=500)
frame1.pack()

frame2 = Frame(window_2, width=10, height=10)
frame2.pack(side='left', anchor=N)

frame3 = Frame(window_2, width=50, height=100)
frame3.pack(side='left', anchor=N)

frame4 = Frame(window_2, width=50, height=100)
frame4.pack(side='left', anchor=N)

lbl_hist = ttk.Label(frame2, text="History:")
lbl_hist.grid(row=0, column=0, sticky="w", padx=20)

list_history = Text(frame2, height=32, width=49, font=50)
list_history.grid(row=1, column=0, sticky="sn", padx=20)

list_history.bind("<Button-3>", do_popup)

m = Menu(window_2, tearoff=0)
m.add_command(label="Search", command=search_tool)

lbl_suggested = ttk.Label(frame1, text="Press 'Get kanji' to start", width=20, font=('Arial', 50))
lbl_suggested.configure(anchor='center')
lbl_suggested.grid(row=0, column=0)

lbl_hist = ttk.Label(frame2, text="History:")
lbl_hist.grid(row=0, column=0, sticky="w", padx=20)

list_history = Text(frame2, height=32, width=49, font=50)
list_history.grid(row=1, column=0, sticky="sn", padx=20)

lbl_space = ttk.Label(frame3, text='')
lbl_space.grid(row=5, column=0, pady=205)

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

lbl_reply = ttk.Label(frame3, text="Spelling:")
lbl_reply.grid(row=1, column=0, sticky="w")

ent_answer_spelling = ttk.Entry(frame3, font=50)
ent_answer_spelling.grid(row=1, column=0)

lbl_reply = ttk.Label(frame3, text="Translation:")
lbl_reply.grid(row=2, column=0, sticky="w")

ent_answer_translation = ttk.Entry(frame3, font=50)
ent_answer_translation.grid(row=2, column=0)

lbl_score = ttk.Label(frame3, text="Score")
lbl_score.configure(anchor='center')
lbl_score.grid(row=3, column=0, sticky="w")

btn_submit = ttk.Button(frame3, text="Submit", width=30, command=checker)
btn_submit.grid(row=3, column=0)

btn_rand_kanji = ttk.Button(frame3, text="Get kanji", width=12, command=random_kanji)
btn_rand_kanji.grid(row=1, column=0, sticky=E)

btn_curr_check = ttk.Button(frame3, text="Lookup kanji", width=12, command=check_curr)
btn_curr_check.grid(row=2, column=0, sticky=E)

lbl_log = ttk.Label(frame4, text="Updates:")
lbl_log.grid(row=0, column=0, sticky="w", padx=20)

list_log = Text(frame4, height=32, width=50, font=50)
list_log.grid(row=1, column=0, sticky="sn", padx=20)

window_2.mainloop()

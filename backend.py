import random
from alphabet_detector import AlphabetDetector
import requests
import logging
import inspect

geometry_param = "770x500"
menu_options = ['Random mode', 'Chain mode', 'Vocabulary practise', 'Settings(In Development)']
log_file_name = 'vocab_log.log'
error_counter = 0
store_jlpt_lvl = ''
url = "https://jisho.org/search/"

logging.basicConfig(filename=log_file_name, format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def logger_file():
    with open(log_file_name, 'r', encoding="utf-8") as error_log:
        content = error_log.read()
        return content


def json_request(word):
    return requests.get("https://jisho.org/api/v1/search/words?keyword=" + word).json()


def error_handler(word):
    global error_counter
    if len(word) == 0:
        error_counter += 1
        logger.error(f'{error_counter}) Trying to submit empty answer\n')
        return False
    elif word == 'empty data':
        error_counter += 1
        logger.error(f"{error_counter}) Entered answer doesn't exist\n")
        return False
    return True


def length_printable(word, response):
    global error_counter
    if len(response['data']) == 0:
        return error_handler('empty data')
    else:
        check_other_forms = response['data'][0]['japanese']
        for i in range(0, len(check_other_forms)):
            if word == check_other_forms[i]['word']:
                return word



def total_score_open_file():
    with open('score.txt', 'r') as f:
        total_score_for_achievement_count = int(f.read())
        return total_score_for_achievement_count


def total_score_add(total_score_for_achievement_count):
    with open('score.txt', 'w') as f:
        total_score_for_achievement_count += 1
        f.write(str(total_score_for_achievement_count))


# get JLPT levels and check for their validity(result is passed to random kanji)
jlpt_1_5 = ['1', '2', '3', '4', '5']


def get_jlpt_lvl(jlpt_from, jlpt_to):
    global store_jlpt_lvl
    global error_counter
    jlpt_storage = ''
    if jlpt_from not in jlpt_1_5 or jlpt_to not in jlpt_1_5:
        error_counter += 1
        logger.error(
            f'{error_counter}) An error occurred, it maybe that something other than a number was provided. '
            f'Numbers must be between 1 and 5\n')
    else:
        int_jlpt_from = int(jlpt_from)
        int_jlpt_to = int(jlpt_to)
        if int_jlpt_to > int_jlpt_from:
            error_counter += 1
            logger.error(f'{error_counter}) JLPT level from must be higher than JLPT level to\n')
        else:
            jlpt_range = range(int_jlpt_to, int_jlpt_from + 1)
            for i in jlpt_range:
                jlpt_storage += str(i)
        store_jlpt_lvl = jlpt_storage
    return store_jlpt_lvl



def random_kanji():
    global error_counter

    if len(store_jlpt_lvl) == 0:
        error_counter += 1
        logger.error(f'{error_counter}) Please adjust JLPT level\n')
    else:
        filename = inspect.stack()[1].filename
        file_name = filename.split('/')
        if file_name[-1] == 'menu3.py':
            lines = open(f'C:/Users/daemo/PycharmProjects/JapaneseDictGame/jlpt vocab/{store_jlpt_lvl[::-1]}.txt',
                         encoding="utf-8").read().splitlines()
            random_choice = random.choice(lines)
            return random_choice
        else:
            lines = open(f'C:/Users/daemo/PycharmProjects/JapaneseDictGame/jlpt kanji/{store_jlpt_lvl[::-1]}.txt',
                         encoding="utf-8").read().splitlines()
            random_choice = random.choice(lines)
            return random_choice


def symbol_check(answer):
    global error_counter
    ad = AlphabetDetector()
    # putting chars into a list to iterate over each one and compare with AlphabetDetector()
    new_list = [x for x in answer]
    # selecting mode: hiragana, katakana or both included. depending on the answer
    for x in new_list:
        result = ad.only_alphabet_chars(x, "CJK")
        result2 = ad.only_alphabet_chars(x, "HIRAGANA")
        result3 = ad.only_alphabet_chars(x, "KATAKANA")
        if result is True or result2 is True:
            return True
        elif result is False or result2 is False:
            error_counter += 1
            logger.error(f'{error_counter} ) Bad entry\n')
            return False
    return True

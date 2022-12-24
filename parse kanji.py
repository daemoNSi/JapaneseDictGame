from PyPDF2 import PdfFileReader
from alphabet_detector import AlphabetDetector

ab = AlphabetDetector()
listlist = []
symbol = '–'
count = 0
my_list = [str(i) for i in range(0, 100)]
my_set = set()

# to parse only kanji
with open('KanjiList.N1.pdf', 'rb') as f:
    reader = PdfFileReader(f)
    NumPages = reader.getNumPages()
    # result = ad.only_alphabet_chars(new_list[x], "CJK")
    for x in range(0, NumPages):
        obje = reader.getPage(x)
        texti = obje.extractText()
        kek = texti.split()
        for i in kek:
            result = ab.only_alphabet_chars(i, "CJK")
            result2 = ab.only_alphabet_chars(i, "HIRAGANA")
            if result == True and i != symbol and i not in my_list:
                # print(i)
                my_set.add(i)


with open('jlpt-n1 kanji.txt', 'w', encoding='utf-8') as f:
    for i in my_set:
        adding = f.write(i+'\n')

#################################################################################################################
import string

exclude = string.printable
new_set = set()

# to parse kanji + hiragana, katakana
with open(f'VocabList.N2.pdf', 'rb') as f:
    read_pdf = PdfFileReader(f)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(0, number_of_pages):
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        kek = page_content.split()
        for i in kek:
            for n in i:
                result = ab.only_alphabet_chars(i, "HIRAGANA")
                result2 = ab.only_alphabet_chars(i, "KATAKANA")
                if n not in exclude and result is False and result2 is False:
                    new_set.add(i)
                    if n == 'お':
                        if result is False and result2 is False:
                            new_set.add(i)
sorted_set = sorted(new_set)


with open(f'jlpt-n2 vocabulary.txt', 'w', encoding='utf-8') as f:
    for i in sorted_set:
        adding = f.write(i+'\n')

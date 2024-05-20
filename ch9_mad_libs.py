# read text file
# let the user replace the following words if they appear in the text file: ADJECTIVE, NOUN, ADVERB or VERB

import os, pyinputplus, re
from pathlib import Path

replaceble_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

open_file = open(Path(os.getcwd()) / 'madlibs.txt')
p = (Path(os.getcwd()) / 'madlibs.txt')
contents = open_file.read()
contents_before = contents.split()
word_index = -1

to_append = ''

for i in contents_before:
    suffix_non_letters = 0
    if not i[-1].isalpha():
        suffix_non_letters = 1
        to_append = i[-1]
        i = i[:-1]
    word_index += 1
    if i in replaceble_words:
        if i == 'ADJECTIVE':
            contents_before[word_index] = pyinputplus.inputStr('Enter a adjective: ')
        elif i == 'NOUN':
            contents_before[word_index] = pyinputplus.inputStr('Enter a noun: ')
        elif i == 'ADVERB':
            contents_before[word_index] = pyinputplus.inputStr('Enter a adverb: ')
        elif i == 'VERB':
            contents_before[word_index] = pyinputplus.inputStr('Enter a verb: ')
        if to_append != '':
            contents_before[word_index] += to_append
            to_append = ''
            print(contents_before[word_index])

finnished_phrase = ' '.join(contents_before)
p.write_text(finnished_phrase)

open_file.close()

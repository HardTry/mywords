# coding=utf-8

import sys, io
import codecs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print('中文')

# file -I 'file-name'
# iconv -f encoding -t encoding < file.old > file.new
# iconv -f utf-161e -t utf-8 < p.txt > u.txt
WORDs_FILE = './u.txt'


class Word:
    def __init__(self, word=''):
        self.word = word
        self.pronon = ''
        self.interp = []  # interpretations
        self.time = 0


def get_dict(filepath):
    # filepath = 'E:\\planet\\english\\PET-words-1.txt'
    # outpath = 'E:\\planet\\english\\word-only.txt'

    word = Word()
    mydict = {}
    all_words = []
    alpha = ''
    with codecs.open(filepath, 'r', encoding='utf-8') as fp:
        for line in fp:
            if line.startswith('+'):
                alpha = line[1: len(line) - 2]
                word = Word(alpha)
                all_words.append(alpha)
            elif line.startswith('#'):
                word.interp.append(line[1: len(line) - 2])
            elif line.startswith('&'):
                word.pronon = line[1: len(line) - 2]
            elif line.startswith('@'):
                word.time = int(line[1: len(line) - 2])
            elif line.startswith('$1'):
                mydict[alpha] = word

    return mydict, all_words


mydict, all_words = get_dict(WORDs_FILE)
print(mydict[all_words[0]])
print(mydict[all_words[-1]])

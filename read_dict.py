# coding=utf-8

import sys, io
import codecs
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print('中文')

# file -I 'file-name'
# iconv -f encoding -t encoding < file.old > file.new
# iconv -f utf-161e -t utf-8 < p.txt > u.txt
WORDs_FILE = './u.txt'

mydict = {}
all_words = []


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Word:
    def __init__(self, word=''):
        self.word = word
        self.pronon = ''
        self.interp = []  # interpretations
        self.time = 0

    def output(self):
        print(self.word, self.pronon)
        for itp in self.interp:
            print(itp)

    def output_interpretation(self):
        for itp in self.interp:
            print(itp)


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


def get_int_input(msg):
    myinput = input(msg)
    if myinput == 'q' or myinput == 'Q': exit(0)
    return int(myinput)


def print_words(words):
    for w in words:
        mydict[w].output()


def select_task():
    print('\nPlease Select Your Task:\n\t1. Practice\n\t2. Examination\n\t3. Quit')
    return get_int_input('Enter your task(1, 2 or 3): ')


def practice():
    print(chr(27) + "[2J")

    words = list(range(0, len(all_words)))
    random.shuffle(words)
    ALL_TIMES = 5
    for w in words:
        mydict[all_words[w]].output()
        times = 0
        while times < ALL_TIMES:
            my_word = input('Enter the word: ')
            if my_word == mydict[all_words[w]].word:
                times += 1
            elif my_word == 'q':
                exit(1)


def exam():
    print(chr(27) + "[2J")

    words = list(range(0, len(all_words)))
    random.shuffle(words)
    score = 0
    for w in words:
        mydict[all_words[w]].output_interpretation()
        my_word = input('Enter the word: ')
        if my_word == mydict[all_words[w]].word:
            print(bcolors.OKGREEN + 'Good!' + bcolors.ENDC)
            score += 1
        elif my_word == 'q':
            exit(2)
        else:
            print(bcolors.FAIL + 'Wrong!' + bcolors.ENDC,\
                  'The correct answer is',\
                  bcolors.OKBLUE + mydict[all_words[w]].word + bcolors.ENDC)

    print('You have got ', bcolors.FAIL + str(float(score / len(all_words) * 100)) + bcolors.ENDC)


if __name__ == '__main__':
    mydict, all_words = get_dict(WORDs_FILE)
    # for w in all_words:
    #     mydict[w].output()

    print('Please Select A Range of Words. We have', len(all_words), 'words.')
    start_index = get_int_input('Enter the start index of word(q for quit): ') - 1
    end_index = get_int_input('Enter the end index of word (q for quit): ')
    all_words = all_words[start_index: end_index]

    task = 0
    while task != 3:
        task = select_task()
        if task == 1:
            practice()
        elif task == 2:
            exam()

    print('\n', bcolors.OKBLUE + 'Goodbye! See you next time!' + bcolors.ENDC + '\n')

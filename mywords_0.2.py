# coding=utf-8

import sys, io, os
import codecs
import random
from colorama import Fore, Back, Style, init
import copy


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print('中文')

# file -I 'file-name'
# iconv -f encoding -t encoding < file.old > file.new
# iconv -f utf-161e -t utf-8 < p.txt > u.txt
WORDs_FILE = './u.txt'

my_dict = {}
all_words = []
unknown = []


class Word:
    def __init__(self, word=''):
        self.word = word
        self.pronon = ''
        self.interp = []  # interpretations
        self.time = 0

    def output(self):
        print('\n', Fore.GREEN + self.word, Fore.RESET + self.pronon)
        for itp in self.interp:
            print(itp)

    def output_interpretation(self):
        for itp in self.interp:
            print(itp)


def get_dict(filepath):
    # filepath = 'E:\\planet\\english\\PET-words-1.txt'
    # outpath = 'E:\\planet\\english\\word-only.txt'

    word = Word()
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
                my_dict[alpha] = word


def get_int_input(msg):
    my_input = input(msg)
    if my_input == 'q' or my_input == 'Q':
        exit(0)
    return int(my_input)


def print_words(words):
    for w in words:
        my_dict[w].output()


def select_task():
    print('\nPlease Select Your Task:\n\t1. Practice\n\t2. Examination\n\t3. Quit')
    if len(unknown) < 1:
        return get_int_input('Enter your task(1, 2 or 3): ')
    else:
        print('\t4. Practice words words\n\t5. Exam wrong words')
        return get_int_input('Enter your task(1, 2 , 3, 4 or 5): ')


def practice(word_list):
    os.system('cls' if os.name == 'nt' else 'clear')

    words = list(range(0, len(word_list)))
    random.shuffle(words)
    all_times = 5
    for w in words:
        my_dict[word_list[w]].output()
        times = 0
        while times < all_times:
            my_word = input('Enter the word: ')
            if my_word == my_dict[word_list[w]].word:
                times += 1
            elif my_word == 'q':
                exit(1)


def exam(word_list):
    os.system('cls' if os.name == 'nt' else 'clear')

    words = list(range(0, len(word_list)))
    random.shuffle(words)
    score = 0
    for w in words:
        my_dict[word_list[w]].output_interpretation()
        my_word = input('Enter the word: ')
        if my_word == my_dict[word_list[w]].word:
            print(Fore.GREEN + 'Good!!!')
            print(Style.RESET_ALL)
            score += 1
        elif my_word == 'q':
            exit(2)
        else:
            print(Fore.RED + 'Wrong!', Fore.RESET + 'The correct answer is', Fore.CYAN + my_dict[word_list[w]].word)
            unknown.append(my_dict[word_list[w]].word)
            print(Style.RESET_ALL)

    print('You have got ', Fore.RED + str(float(score / len(all_words) * 100)))
    print(Style.RESET_ALL)


if __name__ == '__main__':
    init()

    get_dict(WORDs_FILE)
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
            practice(all_words)
        elif task == 2:
            exam(all_words)
        elif task == 4:
            practice(unknown)
        elif task == 5:
            un = copy.copy(unknown)
            unknown = []
            exam(un)

    print('\n', Fore.CYAN + 'Goodbye! See you next time!', '\n')
    print(Style.RESET_ALL)

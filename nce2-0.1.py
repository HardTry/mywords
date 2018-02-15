import sys, io, os
import codecs
import random
from colorama import Fore, Back, Style, init
import copy


# file -I 'file-name'
# iconv -f encoding -t encoding < file.old > file.new
# iconv -f utf-161e -t utf-8 < p.txt > u.txt
# WORDs_FILE = './u.txt'


text_file = './nce2-full.txt'


def get_text(filepath):
    # filepath = 'E:\\planet\\english\\PET-words-1.txt'
    # outpath = 'E:\\planet\\english\\word-only.txt'

    with codecs.open(filepath, 'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('Lesson'):
                print(line)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # print('中文')

    get_text(text_file)
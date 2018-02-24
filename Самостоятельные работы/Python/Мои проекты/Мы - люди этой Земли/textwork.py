﻿import re
import time
import sys


def cntt(text, centers='center'):
    sentences = []
    s = re.sub(r'\s+', ' ', text)
    for s in re.split(r'(?<=[.!?…]) ', s):
        sentences.append(s)

    for s in sentences:
        if centers == "left":
            print('{:<80}'.format(s), end='')
        elif centers == "right":
            print('{:>80}'.format(s), end='')
        elif centers == "center":
            print('{:^80}'.format(s), end='')


def cnt(text, centers='center'):
    if centers == "left":
        print('{:<80}'.format(text), end='')
    elif centers == "right":
        print('{:>80}'.format(text), end='')
    elif centers == "center":
        print('{:^80}'.format(text), end='')


def horiz():
    print('\n--------------------------------------------------------------------------------')


def cls():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def said(phraze):
    bore = False
    time.sleep(0.5)
    for s in phraze:
        print(s, end='')
        sys.stdout.flush()
        if (bore and s == '.') or s == '!':
            time.sleep(0.25)
        else:
            time.sleep(0.04)
        if s == '.':
            bore = True
    print('\n')


def quest(question, ans1='', ans2='', ans3=''):
    result = -1
    print(question + ' (в ответ вводится цифра)')
    print('1. ' + ans1)
    print('2. ' + ans2)
    maxa = 2

    if ans3 != '':
        print('3. ' + ans3)
        maxa = 3

    while result == -1:
        try:
            result = int(input('Ваш ответ: '))
            if result > maxa or result <= 0:
                raise Exception
        except Exception:
            result = -1
            print('Вводите ЧИСЛА от 1 до ' + str(maxa) + '!')
    return result

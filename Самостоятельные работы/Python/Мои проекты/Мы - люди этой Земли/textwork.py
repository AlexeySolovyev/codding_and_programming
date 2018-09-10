import re
import time
import sys
import msvcrt
import os
import random

clear = lambda: os.system('cls')


def cntt(text, centers = 'center'):
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


def cnt(text, centers = 'right'):
    if centers == "left":
        print(text.ljust(80))
    elif centers == "right":
        print(text.rjust(80))
    elif centers == "center":
        print('{:^80}'.format(text), end='')
    sys.stdout.flush()

    time.sleep(1.5)


def horiz():
    print('\n--------------------------------------------------------------------------------')


def cls():
    clear()


def said(phraze):
    bore = False
    situation = False
    sys_space = False
    time.sleep(0.5)
    for s in phraze:
        print(s, end='')
        sys.stdout.flush()
        if (bore and s == '.') or s == '!':
            time.sleep(0.25)
        elif situation:
            time.sleep(0)
        elif sys_space and s == ' ':
            time.sleep(0)
        else:
            time.sleep(0.049)
        if s == '.':
            bore = True
        else:
            bore = False

        if s == '[':
            situation = True
        elif s == ']':
            situation = False
            time.sleep(1)

        if s == ' ':
            sys_space = True
        else:
            sys_space = False

    print('\n')


def wait(text = 'Нажмите любую клавишу...'):
    print(text, end='', flush=True)
    msvcrt.getch()
    print('\b' * len(text) + ' ' * len(text), end='\n', flush=True)


def quest(question, bag, plans, ans1='', ans2='', ans3='', ans4=''):
    result = -1
    print(question + ' (в ответ вводится цифра)')
    print('[1] - ' + ans1)
    maxa = 1

    if ans2 != '':
        print('[2] - ' + ans2)
        maxa = 2
        if ans3 != '':
            print('[3] - ' + ans3)
            maxa = 3
            if ans4 != '':
                print('[4] - ' + ans4)
                maxa = 4

    while result == -1:
        try:
            result = input('Ваш ответ: ')
            if result not in ['B', 'b', 'P', 'p']:
                result = int(result)
            else:
                if result in ['B', 'b']:
                    print('Вот, что храниться в вашем рюкзаке:')
                    for t in bag:
                        print(t)
                    print('\n')
                if result in ['P', 'p']:
                    print('Ваши текущие цели:')
                    for p in plans:
                        print(p)
                    print('\n')
                result = -1
            if result > maxa or result <= 0:
                raise Exception
        except Exception:
            result = -1
            print('Вводите ЧИСЛА от 1 до ' + str(maxa) + '!')
    return result


def yon(winRange):  # yes or no
    randint = random.randint(0, 100)
    if 0 <= randint <= winRange:
        return True


def restart():
    horiz()
    cntt('ИГРА ОКОНЧЕНА!', 'center')
    horiz()

    repeat = input('Хотите продолжить игру с последней главы? ')
    if repeat in ['да', 'Да', 'Д', 'д', 'yes', 'Yes', 'Y', 'y']:
        return True
    else:
        return False

def bagAndPlans(bag, plans):
    print('Вот, что храниться в вашем рюкзаке:')
    for t in bag:
        print(t)
    print('\n')
    print('Ваши текущие цели:')
    for p in plans:
        print(p)
    print('\n')
    time.sleep(5)

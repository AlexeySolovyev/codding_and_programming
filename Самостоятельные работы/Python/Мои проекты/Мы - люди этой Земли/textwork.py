import re
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
    return


def cnt(text, centers='center'):
    if centers == "left":
        print('{:<80}'.format(text), end='')
    elif centers == "right":
        print('{:>80}'.format(text), end='')
    elif centers == "center":
        print('{:^80}'.format(text), end='')
    return


def horiz():
    print('\n--------------------------------------------------------------------------------')


def cls():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def said(phraze):
    bore = False
    time.sleep(1.5)
    for s in phraze:
        print(s, end='')
        sys.stdout.flush()
        if (bore and s == '.') or s == '!':
            time.sleep(0.5)
        else:
            time.sleep(0.1)

        if s == '.':
            bore = True

    print('\n')

# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# 112+6*3/2*5-2

# 1 вариант

from decimal import Decimal
from sympy import sympify

expr = input('Введите пример: ').strip()
print(f'{expr} = {sympify(expr)}')


# 2 вариант
#Решение без ()

import sys

text = input('Введите пример: ').replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ').split()


def prod():
    for j in range(len(text)):
        if j == text.index('*'):
            text[j] = str(Decimal(text[j - 1]) * Decimal(text[j + 1]))
            text.pop(j + 1)
            text.pop(j - 1)
            break


def div():
    for j in range(len(text)):
        if j == text.index('/'):
            if Decimal(text[j + 1]) == 0:
                print('На ноль делить нельзя!')
                sys.exit()
            else:
                text[j] = str(Decimal(text[j - 1]) / Decimal(text[j + 1]))
                text.pop(j + 1)
                text.pop(j - 1)
                break


def summ():
    for j in range(len(text)):
        if j == text.index('+'):
            text[j] = str(Decimal(text[j - 1]) + Decimal(text[j + 1]))
            text.pop(j + 1)
            text.pop(j - 1)
            break


def dif():
    for j in range(len(text)):
        if j == text.index('-'):
            text[j] = str(Decimal(text[j - 1]) - Decimal(text[j + 1]))
            text.pop(j + 1)
            text.pop(j - 1)
            break


for i in range(len(text)):
    while len(text) > 1:
        while '*' in text or '/' in text:
            if len(text) == 1:
                print('Результат вычисления= ', *text, sep='')
                break
            elif '*' in text and '/' in text:
                p = text.index('*')
                d = text.index('/')
                if p < d:
                    prod()
                elif p > d:
                    div()
            elif '*' not in text:
                div()
            elif '/' not in text:
                prod()
            elif not '*' and '/' in text:
                break
        while '+' or '-' in text:
            if len(text) == 1:
                print('Результат вычисления= ', *text, sep='')
                break
            if '+' in text and '-' in text:
                s = text.index('+')
                d = text.index('-')
                if s < d:
                    summ()
                elif s > d:
                    dif()
            elif '+' not in text:
                dif()
            elif '-' not in text:
                summ()
            elif '+' not in text and '-' not in text:
                break
    else:
        break
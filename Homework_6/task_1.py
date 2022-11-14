# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# 112+6*3/2*5-2

import sys

text = input('Введите пример: ').replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ').split()

def prod(prod_num):
    for i in range(len(text)):
        if i == text.index('*'): 
            prod_num = str(float(text[i-1]) * float(text[i+1]))
            a = text.index('*')
            text.pop(a-1)
            a = text.index('*')
            text.pop(a+1)
            text.insert(i, prod_num)
            a = text.index('*')
            text.pop(a)
            break

def div(div_num):
    for i in range(len(text)):
        if i == text.index('/'):
            if int(text[i+1]) == 0:
                print('На ноль делить нельзя!')
                sys.exit()
            else:
                div_num = str(float(text[i-1]) / float(text[i+1]))
                a = text.index('/')
                text.pop(a-1)
                a = text.index('/')
                text.pop(a+1)
                text.insert(i, div_num)
                a = text.index('/')
                text.pop(a)
                break


def sum(sum_num):
    for i in range(len(text)):
        if i == text.index('+'): 
            sum_num = str(float(text[i-1]) + float(text[i+1]))
            a = text.index('+')
            text.pop(a-1)
            a = text.index('+')
            text.pop(a+1)
            text.insert(i, sum_num)
            a = text.index('+')
            text.pop(a)
            break

def dif(diff_num):
    for i in range(len(text)):
        if i == text.index('-'):
            diff_num = str(float(text[i-1]) - float(text[i+1]))
            a = text.index('-')
            text.pop(a-1)
            a = text.index('-')
            text.pop(a+1)
            text.insert(i, diff_num)
            a = text.index('-')
            text.pop(a)
            break

for i in range(len(text)):
    while len(text) > 1:
        while '*' in text or '/' in text:
            if len(text) == 1:
                print('Результат вычисления= ', *text, sep= '')
                break
            elif '*' in text and '/' in text:
                p = text.index('*')
                d = text.index('/')
                if p < d:
                    prod(text) 
                elif p > d:
                    div(text)
            elif '*' not in text:
                div(text)
            elif '/' not in text:
                prod(text)
            elif not '*' and '/' in text:
                break
        while '+' or '-' in text:
            if len(text) == 1:
                print('Результат вычисления= ', *text, sep= '')
                break
            if '+' in text and '-' in text:
                s = text.index('+')
                d = text.index('-')
                if s < d:
                    sum(text) 
                elif s > d:
                    dif(text)
            elif '+' not in text:
                dif(text)
            elif '-' not in text:
                sum(text)
            elif not '+' in text and not '-' in text:
                break      
    else:
        break
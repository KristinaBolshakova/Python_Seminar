# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


num = int(input('Введите число N: '))
num_list = []

while num % 2 == 0:
    num_list.append(2)
    # print(2)
    num = num / 2
for i in range(3, int(math.sqrt(num)) +1, 2):
    while(num % i == 0):
        num_list.append(i)
        # print(i)
        num = num / i
if num>2:
    num_list.append(int(num))
    # print(num)
print(f'Простые множетели числа N: {num_list}')
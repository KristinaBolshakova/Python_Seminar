# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

import random
from random import uniform

num = int(input('Введите количество чисел в списке: '))
list = []

for i in range(num):
    rand = random.uniform(0, 10)
    and_round = round(rand, 2)
    list.append(and_round)

min = 1
max = 0
for i in list:
    elem = i - int(i)
    if elem <= min:
        min = elem 
    if elem >= max:
        max = elem

diff = max-min

print(list)
print(round((diff), 2))




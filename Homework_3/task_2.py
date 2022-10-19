# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

num = int(input('Введите количество чисел в списке: '))
list1 = []
list2 = []

for i in range(num):
    list1.append(randint(0, 9))

for i in range(len(list1)):
    while i < len(list1)/2 and num > len(list1)/2:
        num = num - 1
        a = list1[i] * list1[num]
        list2.append(a)
        i += 1

print(list1)
print(list2)

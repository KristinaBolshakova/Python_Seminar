# # Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых  и убрать дубликаты из заданной последовательности.
# # Пример:
# # [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]
# #Вариант 1

from random import randint


num = int(input('Введите количество чисел в списке: '))
N1 = int(input('Введите диапазон чисел для заполнения от: '))
N2 = int(input('до: '))

rand_list=[]

for i in range(num):
    rand_list.append(randint(N1, N2))
print(f'Последовательность случайных чисел: {rand_list}\n')

print('Вариант 1\n')

unik_list = [i for i in set(rand_list) if rand_list.count(i) == 1]
dubl_elem_list = list(set(rand_list) - set(unik_list))
no_duble_list = list(set(rand_list))

print(f'''Неповторяющиеся элементы в исходной последовательности: {unik_list}
Повторяющиеся элементы: {dubl_elem_list}
Последовательность чисел без дубликатов: {no_duble_list}\n''')

#Вариант 2

print('Вариант 2\n')

list_1 = rand_list
list_2 = []
list_3 = []

# for i in range(num):
#     list_1.append(randint(N1, N2))
# print(f'Последовательность случайных чисел: {list_1}\n')

for i in list_1:
    if i not in list_3:
        list_3.append(i) 

for i in list_1:
  if list_1.count(i) != 1:
    list_2.append(i)
    
    for j in list_1[::-1]:
      if j == i:
        list_1.remove(j) 

print(f'''Неповторяющиеся элементы в исходной последовательности: {list_1}   
Повторяющиеся элементы: {list_2}
Последовательность чисел без дубликатов: {list_3}''')
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from random import randint

k = int(input('Введите натуральную степень k = '))
data = open('Homework_4.txt', 'w')

list_ratio = []
new_list = []
for i in range(k+1):
    list_ratio.append(randint(0, 100))
print(f'Список случайных коэффициентов: {list_ratio}')
print()
new_list.append(f'k = {k} => ')
for i in list_ratio:
    print(f'{i}*x**{k}', end = ' + ')
    new_list.append(f'{i}*x**{k} + ')
    k -= 1
    if k == 0:
        break
print(f'{list_ratio[-1]}', end = ' = 0')
new_list.append(f'{list_ratio[-1]} = 0' )
print(new_list)

data.writelines(new_list)
data.close

exit()
        



    
   















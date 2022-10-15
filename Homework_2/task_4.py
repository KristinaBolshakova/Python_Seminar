# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
num_list = []
for i in range(-N, N+1):
    num_list.append(i)
print(num_list)

prod = 1
new_list = []

f = open('file.txt', 'r')
for line in f:
    if int(line) < len(num_list):
        prod *= num_list[int(line)]
        new_list.append(num_list[int(line)])

print(new_list)

print('Произведение элементов на указанных позициях =', prod if prod != 1 else 'Значения не найдены')
















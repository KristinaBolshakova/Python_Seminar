# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

get_list = ['2', '3', '5', '9', '3']
sum = 0

for i in range(len(get_list)):
    if i % 2 != 0:
        sum += int(get_list[i])

print(sum)










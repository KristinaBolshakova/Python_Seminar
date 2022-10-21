# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# from random import randint

# k = int(input('Введите натуральную степень k = '))
# data_1 = open('Homework_4-1.txt', 'w')

# list_ratio = []
# new_list_f1 = []
# for i in range(k+1):
#     list_ratio.append(randint(0, 100))
# print(f'Список случайных коэффициентов: {list_ratio}')
# print()
# # new_list_f1.append(f'k = {k} => ')
# for i in list_ratio:
#     print(f'{i}x^{k}', end = ' + ')
#     new_list_f1.append(f'{i}x^{k} + ')
#     k -= 1
#     if k == 0:
#         break
# print(f'{list_ratio[-1]}', end = ' = 0')
# new_list_f1.append(f'{list_ratio[-1]} = 0' )
# # print(new_list)

# data_1.writelines(new_list_f1)
# data_1.close
# exit()

path = 'Homework_4.txt'
data = open(path, 'r')
for line in data:
    print(line)
    

path_1 = 'Homework_4-1.txt'
data_1 = open(path_1, 'r')
for line_1 in data_1:
    print(line_1)

data.close()
data_1.close()

data_2 = open('Homework_4-2.txt', 'w')

# sum = 0            
# if sum = int(line[0])+int(line_1[0])
# print(sum)


# import re
# s = line
# nums = re.findall(r'\d+', s)
# nums = [int(i) for i in nums]
# print(nums)

data_2.close
exit()

from random import randint

k = int(input('Введите натуральную степень k = '))
data_1 = open('Homework_4-1.txt', 'w')

list_ratio = []
new_list_f1 = []
for i in range(k+1):
    list_ratio.append(randint(0, 100))
print(f'Список случайных коэффициентов: {list_ratio}')
print()
# new_list_f1.append(f'k = {k} => ')

for i in list_ratio:
    print(f'{i}x^{k}', end = ' + ')
    new_list_f1.append(f'{i}x^{k} + ')
    k -= 1
    if k == 0:
        break
print(f'{list_ratio[-1]}', end = ' = 0')
new_list_f1.append(f'{list_ratio[-1]} = 0' )
# print(new_list)

data_1.writelines(new_list_f1)
data_1.close
exit()
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# создание многочлена в виде строки 
def pol_line(line):
    lst= line[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# запись в файл
def write_file(name,form):
    with open(name, 'w') as data:
        data.write(form)

# получение степени многочлена
def deg_pol(deg):
    if 'x^' in deg:
        pos = deg.find('^')
        num = int(deg[pos+1:])
    elif ('x' in deg) and ('^' not in deg):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def rat_pol(rat):
    if 'x' in rat:
        i = rat.find('x')
        num = int(rat[:i])
    return num

# разбор многочлена и получение его коэффициентов
def del_mnog(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if deg_pol(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if deg_pol(st[ii]) != -1 and deg_pol(st[ii]) == i:
            lst.append(rat_pol(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    
# нахождение суммы многочлена
with open('Homework_4.txt', 'r') as data:
    pol_1 = data.readlines()
with open('Homework_4-1.txt', 'r') as data:
    pol_2 = data.readlines()
print(f'Первый полином - {pol_1}')
print(f'Второй полином - {pol_2}')
lst1 = del_mnog(pol_1)
lst2 = del_mnog(pol_2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])

write_file('Homework_4-2.txt', pol_line(lst_new))
with open('Homework_4-2.txt', 'r') as data:
    sum_pol = data.readlines()
print(f"Сумма полиномов = {sum_pol}")
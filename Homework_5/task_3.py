# Создайте программу для игры в ""Крестики-нолики"".

from itertools import count
from random import randint


first_name = input('Введите имя первого игрока: ')
second_name = input('Введите имя второго игрока: ')

print('Сперва определим, чей ход. Кидайте кубик, у кого выпадает нечетное число, тот ходит первым.')
rand = randint(1,7)
print(f'Выпало число: {rand}')
if rand % 2 != 0:
    player_1 = first_name
    player_2 = second_name
    print(f'Первым ходит игрок по имени {first_name}. Ваш ход.')
else:
    player_1 = second_name
    player_2 = first_name
    print(f'Первым ходит игрок по имени {second_name}. Ваш ход. ')


mas = [['-' for i in range(3)] for j in range(3)]

def print_mas(mas_2):
    for i in mas_2:
        print(*i)
    return

print_mas(mas)

def you_win(mas_3):
    if (mas_3[0][0] == mas_3[0][1] == mas_3[0][2]) != '-':
        return mas_3[0][0]
    elif (mas_3[1][0] == mas_3[1][1] == mas_3[1][2]) != '-':
        return mas_3[1][0]
    elif (mas_3[2][0] == mas_3[2][1] == mas_3[2][2]) != '-':
        return mas_3[2][0]
    elif (mas_3[0][0] == mas_3[1][0] == mas_3[2][0]) != '-':
        return mas_3[0][0]
    elif (mas_3[0][1] == mas_3[1][1] == mas_3[2][1]) != '-':
        return mas_3[0][1]
    elif (mas_3[0][2] == mas_3[1][2] == mas_3[2][2]) != '-':
        return mas_3[0][2]
    elif (mas_3[0][0] == mas_3[1][1] == mas_3[2][2]) != '-':
        return mas_3[0][0]
    elif (mas_3[2][0] == mas_3[1][1] == mas_3[0][2]) != '-':
        return mas_3[2][0]
    else:
        return False


def step(mas_1, player):
    st, col = int(input('ряд: ')), int(input('столбец: '))
    
    if mas_1[st-1][col-1] == 'X' or mas_1[st-1][col-1] == 'O':
        print('Эта клетка занята, выбирайте другую.')

    elif player == 1:
        mas_1[st-1][col-1] = 'X'
        print_mas(mas_1)

    elif player == 2:
        mas_1[st-1][col-1] = 'O'
        print_mas(mas_1)
    

count = 0
cur_player = 1

while True:
    step(mas, cur_player)
    win = you_win(mas)
    count += 1
    if win == 'X':
        print(f'Победил(а) {player_1}')
        break
    elif win == 'O':
        print(f'Победил(а) {player_2}')
        break
    elif count == 9:
        print('ничья')
        break
    if cur_player == 1:
        cur_player = 2
    else:
        cur_player = 1
        

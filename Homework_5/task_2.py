# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
from turtle import TPen

game_var = int(input('1 - два игрока \n2 - игра с компьютером\nВыберите вариант игры: '))

num = 121
count = 0
max_step = 28

if game_var == 1:
      
    first_name = input('Введите имя первого игрока: ')
    second_name = input('Введите имя второго игрока: ')

    print('Сперва определим, кто ходит первый. Кидайте кубик, у кого выпадает нечетное число, тот ходит первым.')
    rand = randint(1,7)
    print(f'Выпало число: {rand}')
    if rand % 2 != 0:
        player_1 = first_name
        player_2 = second_name
        print(f'Первым ходит игрок по имени {first_name}.\nВаш ход.\nНа столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет')
    else:
        player_1 = second_name
        player_2 = first_name
        print(f'Первым ходит игрок по имени {second_name}. Ваш ход. На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет')

    while num > 0:
        step = int(input('Введите, сколько нужно забрать конфет: '))
        if 0 < step < 29 and step <= num:
            num -= step
            count += 1
            print(f'На столе осталось {num} конфет')
        elif 29 < step < 0:
            print('Неверное число конфет, введите число от 1 до 28.') 
        elif step >= num:
            print(f'Неверное число конфет, введите число от 1 до {num}.') 

    if count % 2 != 0:
        
        print(f'Победил игрок по имени {player_1}')
    else:
        print(f'Победил игрок по имени {player_2}')



elif game_var == 2:

    first_name = input('Введите имя первого игрока: ')
    print('Имя второго игрока: Компьютер')
    second_name = 'Компьютер'

    print('Сперва определим, чей ход. Кидайте кубик, у кого выпадает нечетное число, тот ходит первым.')

    rand = randint(1,7)
    print(f'Выпало число: {rand}')

    if rand % 2 != 0:
        player_1 = first_name
        player_2 = second_name
        print(f'Первым ходит игрок по имени {first_name}.\nВаш ход.\nНа столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет')
    else:
        player_1 = second_name
        player_2 = first_name
        print(f'Первым ходит игрок по имени {second_name}. Ваш ход. На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет')



    if player_1 != 'Компьютер':
        while num > 0:
            step = int(input('Введите, сколько нужно забрать конфет: '))
            if 0 < step < 29 and step < num:
                num -= step
                count += 1
                print(f'На столе осталось {num} конфет')
            elif 29 < step < 0:
                print('Неверное число конфет, введите число от 1 до 28.')
                step = int(input('Введите, сколько нужно забрать конфет: '))
                if 0 < step < 29 and step <= num:
                    num -= step
                    count += 1
                    print(f'На столе осталось {num} конфет')  
            elif step >= num:
                print(f'Неверное число конфет, введите число от 1 до {num}.')
                step = int(input('Введите, сколько нужно забрать конфет: '))
                if 0 < step < 29 and step <= num:
                    num -= step
                    count += 1
                    print(f'На столе осталось {num} конфет') 
            
            if num > max_step and num > 0 :
                step = randint(1,max_step)
                num -= step
                count += 1
                print(f'Компьютер взял {step} конфет. На столе осталось {num} конфет.')
            elif num < max_step and num > 0:
                max_step = num
                step = randint(1,max_step)
                num -= step
                count += 1
                print(f'Компьютер взял {step} конфет. На столе осталось {num} конфет.')
            
        
    else:
        while num > 0:    
            if num > max_step and num > 0 :
                step = randint(1,max_step)
                num -= step
                count += 1
                print(f'Компьютер взял {step} конфет. На столе осталось {num} конфет.')
            elif num < max_step and num > 0:
                max_step = num
                step = randint(1,max_step)
                num -= step
                count += 1
                print(f'Компьютер взял {step} конфет. На столе осталось {num} конфет.')
            
            step = int(input('Введите, сколько нужно забрать конфет: '))
            if 0 < step < 29 and step < num:
                num -= step
                count += 1
                print(f'На столе осталось {num} конфет')
            elif 29 < step < 0:
                print('Неверное число конфет, введите число от 1 до 28.')
                step = int(input('Введите, сколько нужно забрать конфет: '))
                if 0 < step < 29 and step <= num:
                    num -= step
                    count += 1
                    print(f'На столе осталось {num} конфет')  
            elif step >= num:
                print(f'Неверное число конфет, введите число от 1 до {num}.')
                step = int(input('Введите, сколько нужно забрать конфет: '))
                if 0 < step < 29 and step <= num:
                    num -= step
                    count += 1
                    print(f'На столе осталось {num} конфет') 
                
    if count % 2 != 0:
        print(f'Победил игрок по имени {player_1}')
    else:
        print(f'Победил игрок по имени {player_2}')

else:
    print('Такого варианта нет')


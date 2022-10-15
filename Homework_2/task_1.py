# 1 – Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('Введите число: '))
num = float(abs(num))
num_string = str(num)
num_string = num_string.replace('.', '')
sum = 0
for i in num_string:
    sum += int(i)
print(f'Сумма цифр числа {num} =', sum)



# print(sum(map(int, list(".join(c for c in input('Введите число: ') if c.isdecimal)))))
# or isdigit()













# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

num = input('Введите число: ')
d = input('Введите степень округления: ')

print(f'Число, до округления = {num}')
print(f'Степень округдения d = {d}')

number = Decimal(num)
number = number.quantize(Decimal(d))
print(f'Число после округления = {number}') 

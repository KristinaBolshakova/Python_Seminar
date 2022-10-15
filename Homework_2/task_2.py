# 2 –Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N: '))

num = 1
num_list = []
for i in range(1, N+1):              
    num *= i 
    num_list.append(num)

print(num_list)


# from math import factorial
    
# num = [1]
# for i in range(1, N + 1):
#     num.append(i * num[-1])

#     print(num[i], end=" ")


# def factorial(x): return x if x == 1 else x * factorial(x - 1)
    # print([factorial(i) for i in range(1, n + 1)])

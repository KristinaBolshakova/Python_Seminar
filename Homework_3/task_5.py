# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).
# Они также могут быть определены по формуле F−n = (−1)n+1Fn.  

n = int(input('Введите число: '))

fib = []
negafib = []

a, b = 1, 1
for i in range(n):
    fib.append(a)
    a, b = b, a + b
# print(fib) 
a, b = 0, 1
for i in range (n+1):
    negafib.append(a)
    a, b = b, a - b
negafib.reverse()
# print(negafib)
nf = negafib + fib
print(f'для k = {nf}')

    





 





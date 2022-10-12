# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Введите х(0 или 1): '))
# y = int(input('Введите y(0 или 1): '))
# z = int(input('Введите z(0 или 1): '))


# result = 0
# for i in range(1, 9):
#     if (not(x == 1 or y == 1 or z == 1) == (not x == 1 and not y == 1 and not z == 1)):
#         result += 1
#     else:
#         break

#     if (i == 1):
#         x = 0
#         y = 0
#         z = 1
#     elif (i == 2):
#         x = 0
#         y = 1
#         z = 0
#     elif (i == 3):
#         x = 0
#         y = 1
#         z = 1
#     elif (i == 4):
#         x = 1
#         y = 0
#         z = 0
#     elif (i == 5):
#         x = 1
#         y = 0
#         z = 1
#     elif (i == 6):
#         x = 1
#         y = 1
#         z = 0
#     else:
#         x = 1
#         y = 1
#         z = 1

# if result == 8:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')

# list = [0, 0, 0]

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(x, y, z)
            print('Истина' if not (x or y or z) == (not x and not y and not z) else 'Ложь')


# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             print(x,'AND',y,'OR',z,'=',x and y or z)

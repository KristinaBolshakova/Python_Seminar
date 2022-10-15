# 5 – Реализуйте алгоритм перемешивания списка.
  
import random

list_elem = list(range(5))
print(f'Исходный список:\n {list_elem}')
random.shuffle(list_elem)
print(f'Перемешанный список:\n {list_elem}')



# import random

# list_elem = [random.randint(0,10) for i in range(random.randint(0,10))]
# print(f"Исходный список:\n {list_elem}")
# random.shuffle(list_elem)
# print(f"список после перемешивания:\n{list_elem}")
# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв"

# Исправлено!

text = input('Введите текст через пробел и нажмите Enter:\n').split()

frag_1 = 'а'
frag_2 = 'б'
frag_3 = 'в'

text_1 = []

for i in text:
    if frag_1 in i.lower():
        if frag_2 in i.lower():
            if frag_3 in i.lower():
                continue
    text_1.append(i)
              
print('Полученный текст: ')              
print(*text_1, sep=' ')

# Аванс авбанс ваганоаб код мел мАвбб
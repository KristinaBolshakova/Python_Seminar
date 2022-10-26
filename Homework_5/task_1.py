# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв"
print()
text = input('Введите текст через пробел и нажмите Enter:\n').split()
print()
# print(text)

new_text = []

for i in range(len(text)):
    low = text[i].lower()
    new_text.append(low)

frag_1 = 'а'
frag_2 = 'б'
frag_3 = 'в'

text_1 = []

for i in range(len(text)):
    if frag_1 and frag_2 and frag_3 not in text[i]:
        a = text[i]
        text_1.append(a)
              
print('Полученный текст: ')              
print(*text_1, sep=' ')
print()

# аванс авбанс ваганоаб код мел мАбвб
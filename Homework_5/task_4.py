# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE

with open('Homework_5_enter.txt', 'r') as data:
    text_file = data.readlines()

text = ''.join(text_file)
print(f'Исходные данные: {text}')
count = 1
new_text = ''

for i in range(len(text)-1):
    if (text[i] == text[i+1]):
        count += 1
    elif (text[i] != text[i+1]):
        new_text = new_text + str(count) + text[i]
        count = 1
if count > 1 or (text[len(text)-2] != text[-1]):
    new_text = new_text + str(count) + text[-1]

print(f'Сжатый файл: {new_text}')

with open('Homework_5_output.txt', 'w') as data:
        data.write(new_text)

with open('Homework_5_output.txt', 'r') as data:
    new_text_file = data.readlines()

for_dec_text = ''.join(new_text_file)

num = ''
dec_text = ''

for i in range(len(for_dec_text)):
    if not for_dec_text[i].isalpha():
        num += for_dec_text[i]
    else:
        dec_text = dec_text + for_dec_text[i] * int(num)
        num = ''
    
print(f'Восстановленные данные: {dec_text}')    

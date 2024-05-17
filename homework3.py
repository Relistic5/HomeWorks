my_string = input('Напишите что-нибудь: ')

print(f'Количество введенных символов: {len(my_string)}')
print(f'В верхнем регистре {my_string.upper()}')
print(f'В нижнем регистре {my_string.lower()}')
print('Без пробелов', my_string.replace(' ', ''))
print(f'Количество слов {len(my_string.split())}')
print(f'Первый символ {my_string[0]}')
print(f'Последний символ {my_string[-1]}')

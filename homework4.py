immutable_var = (1, 'String', True, ['name', 'phone'])

print(f'Кортеж:\n{immutable_var}')

# immutable_var[1] = 'TwoString' - не сработает

print('------------------')

mutable_list = [1, 'String', True, 'name', 'phone']

print(f'Исходный изменяемый список:\n{mutable_list}')

mutable_list[0] = 2
mutable_list[1] = 'TwoString'
mutable_list[2] = False
mutable_list[3] = 'surname'
mutable_list[4] = 'e-mail'

print(f'Измененный изменяемый список c изменениями)):\n{mutable_list}')

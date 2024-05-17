# Сложная сдача
print('Введите данные о покупке:\n')

name = input('Что покупаем?: ')
price = int(input('Стомость: '))
weight = int(input('Вес: '))
money = int(input('Сколько у Вас денег: '))

if money < price * weight:
  print('\nНе хватает(( Пойди еще поработай')
  print('-------------\n\n')
else:
  print('\nПокупка совершена. Вот Ваш чек:\n\n-------------')
  import datetime
  datetime_object = datetime.datetime.now()
  print(datetime_object)
  print(f'{name} ----- Вес: {weight} кг ----- Стоимость: {price} руб/кг.')
  print(f'     Итого: {price * weight} руб.')
  print(f'Внесено: {money} руб. ----- Сдача: {money - price * weight} руб.')
  print('-------------\n\n')

# ------------------------------------------------------------------------------
# Самая простая задача на свете

n = int(input('Введите число: '))
print('Купи конструктор!\n' * n)

# ------------------------------------------------------------------------------
# Автоматизируем простоту!

do_this = input('Что любите делать?\n')
n = int(input('Сколько раз?'))
print(f'Обожаю {do_this.lower()} !\n' * n)
firstStr = 'Это моя строка'

def delay():
    from time import sleep
    sleep(2)


while True:
    answer = int(input('Выберите действие \n'
                       '1 - Выведите первый символ \n'
                       '2 - Выведите последний символ \n'
                       '3 - Выведите подстроку с третьего по пятый символы \n'
                       '4 - Выведите строку наоборот \n'
                       '5 - Выведите длину строки \n'
                       '6 - Соедините строки \n'
                       '\n'
                       '0 - Выйти из программы \n'))

    if answer not in [1, 2, 3, 4, 5, 6, 0]:
        print("\nНеа.. Попробуйте еще раз.\n ------------------- \n")
        delay()
        continue

    elif answer == 1:
        print('\n  Результат: \n' + firstStr[0] + '\n ------------------- \n')
        delay()

    elif answer == 2:
        print('\n  Результат: \n' + firstStr[-1] + '\n ------------------- \n')
        delay()

    elif answer == 3:
        print('\n  Результат: \n' + firstStr[2:5] + '\n ------------------- \n')
        delay()

    elif answer == 4:
        print('\n  Результат: \n' + firstStr[::-1] + '\n ------------------- \n')
        delay()

    elif answer == 5:
        print('\n  Результат:')
        print(len(firstStr))
        print(' ------------------- \n')
        delay()

    elif answer == 6:
        print('\n  Результат: \n' + 'Это новая строка ' + firstStr + '\n ------------------- \n')
        delay()

    elif answer == 0:
        break

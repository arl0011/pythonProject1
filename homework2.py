from homework import monday

day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))
if (day <1 or day > 31):
    print('введите корректную дату')
elif(month < 1 or month > 12):
    print('введите корректный месяц')
elif(day > 21 and month == 1):
    print('ваш знак зодиака водолей')
elif(day < 19 and month == 2):
    print('ваш знак зодиака водолей')

day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))
if(month in {1,2,5,7,8,10,12} and day > 31)  or (month in {4,6,9,11} and day > 30) or (month == 2 and day > 29) :
    print('введите корректную дату')
elif (month < 1 or month > 12):
    print('введите корректный месяц')
elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
    print('ваш знак зодиака водолей')
elif (day >= 20 and month == 2) or (day <= 20 and month == 3):
    print('ваш знак зодиака рыбы')
elif (day >= 21 and month == 3) or (day <= 20 and month == 4):
    print('ваш знак зодиака овен')
elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
    print('ваш знак зодиака телец')
elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
    print('ваш знак зодиака близнецы')
elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
    print('ваш знак зодиака рак')
elif (day >= 23 and month == 7) or (day <= 21 and month == 8):
    print('ваш знак зодиака лев')
elif (day >= 22 and month == 8) or (day <= 23 and month == 9):
    print('ваш знак зодиака дева')
elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
    print('ваш знак зодиака весы')
elif (day >= 24 and month == 10) or (day <= 22 and month == 11):
    print('ваш знак зодиака скорпион')
elif (day >= 23 and month == 11) or (day <= 22 and month == 12):
    print('ваш знак зодиака стрелец')
elif (day >= 23 and month == 12) or (day <= 20 and month == 1):
    print('ваш знак зодиака козерог')




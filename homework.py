monday = float(input('введите сумму за понедельник: '))
tuesday = float(input('введите сумму за вторник: '))
wednesday = float(input('введите сумму за среду: '))
thursday = float(input('введите сумму за четверг: '))
friday = float(input('введите сумму за пятницу: '))
saturday = float(input('введите сумму за субботу: '))
sunday = float(input('введите сумму за воскресенье: '))

summ = monday+tuesday+wednesday+thursday+friday+saturday+sunday
print(f'общая сумма: {summ}')
average = summ/7
average_rounded = round(average, 1)
print(f'среднее арифметическое: {average_rounded}')
if average >= 1 and average <= 200:
    print('малый расход')
elif average >=201 and average <= 500:
    print('средний расход')
elif average >= 501 :
    print('большой расход')
else:

    print('ничего не потрачено')
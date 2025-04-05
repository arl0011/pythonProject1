data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

# Разделяем элементы на буквы и числа
for item in data_tuple:
    if str(item) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters.append(item)
    else:
        numbers.append(item)

# Удаляем 6.13 и перемещаем True в letters
numbers.remove(6.13)
true_index = numbers.index(True)
numbers.pop(true_index)
letters.append(True)

# Вставляем 2 между 3 и 1
index_one = numbers.index(1)
numbers.insert(index_one, 2)

# Сортируем numbers
numbers.sort()

# Меняем 'g' на 'G' и 'C' на 'c' перед реверсом
letters[letters.index('g')] = 'G'  # Меняем 'g' на 'G'
letters[letters.index('C')] = 'c'  # Меняем 'C' на 'c'

# Реверсируем список letters
letters.reverse()

# Возводим числа в квадрат
numbers = [num ** 2 for num in numbers]

# Преобразуем списки в кортежи
letters = tuple(letters)
numbers = tuple(numbers)

# Вывод результата
print("letters:", letters)
print("numbers:", numbers)






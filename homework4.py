data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for item in data_tuple:
    if str(item) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters.append(item)
    else:
        numbers.append(item)
numbers.remove(6.13)
true_index = numbers.index(True)
numbers.pop(true_index)
letters.append(True)
index_one = numbers.index(1)
numbers.insert(index_one, 2)
numbers.sort()
letters.reverse()
index_g = letters.index('g')
letters[index_g] = 'G'
index_C = letters.index('C')
letters[index_C] = 'c'
numbers = [num ** 2 for num in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print("letters:", letters)
print("numbers:", numbers)
vowels_ru = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowels_en = "aeiouAEIOU"


while True:
    word = input("Введите слово (или 'стоп' для выхода): ")
    if word == "стоп":
        break
    total = 0
    glass_letters = 0
    sogl_letters = 0
    for letter in word:
        total += 1
        if letter in vowels_ru or letter in vowels_en:
            glass_letters += 1
        else:
            sogl_letters += 1
    if total > 0:
        glass_percentage = round(glass_letters / total * 100, 2)
        sogl_percentage = round(sogl_letters / total * 100, 2)
    else:
        glass_percentage = sogl_percentage = 0

    print(f"Слово: {word}")
    print(f"Количество букв: {total}")
    print(f"Согласных букв: {sogl_letters}")
    print(f"Гласных букв: {glass_letters}")
    print(f"Гласные/Согласные: {glass_percentage}% / {sogl_percentage}%")
def get_name_and_age(name: str, birth_year: int):
    age = 2025 - birth_year
    return f"{name}, {age} лет"

name_and_age = get_name_and_age("Арлен",2000)
print(name_and_age)
print(get_name_and_age("Нурадил",1990))


Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']

Geeks['address'] = 'Ибраимова 203'

Geeks['phone'] = '0701052018'
Geeks['instagram'] = '@geeks_edu'

new_courses = {'Data Science', 'AI', 'Cyber Security', 'DevOps'}
print(set(Geeks['courses']) | new_courses)

Geeks['courses'] = set(Geeks['courses']) | new_courses

Geeks['foundation_date'] = '01-01-2000'

print(f"Количество курсов: {len(Geeks['courses'])}")

for key, value in Geeks.items():
    print(f"{key}: {value}")
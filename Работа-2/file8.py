import random

names = open('name.txt', 'r', encoding='utf-8')
surnames = open('surname.txt', 'r', encoding='utf-8')

names = [name.replace("\n", "") for name in names.readlines()]
surnames = [surname.replace("\n", "") for surname in surnames.readlines()]

array_of_surnames = [[] * 4]


def random_part(surname, i):
    try:
        return surname[i * 2:i * 2 + random.choice([2, 3])]
    except:
        return surname[0:random.choice([2, 3])]


for surname in surnames:
    for i in range(4):
        array_of_surnames[i].append(random_part(surname, i))


while True:
    new_name = random.choice(names)
    new_surname = ''.join([random.choice(array_of_surnames[i]) for i in range(random.choice([2, 3, 4]))])
    print(new_name + ' ' + new_surname)
    x = input()
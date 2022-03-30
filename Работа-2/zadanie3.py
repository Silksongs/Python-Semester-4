def generate_group():
    group = 'И{}БО-{}-20'
    letters = {'А': 2, 'В': 13, 'К': 30, 'М': 2, 'Н': 15}
    for i in letters.keys():
        for j in range(1, letters[i] + 1):
            print(group.format(i, j))

generate_group()
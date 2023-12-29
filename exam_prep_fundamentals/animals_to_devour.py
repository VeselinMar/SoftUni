animals = {}
areas = {}

line = input()
while line != 'EndDay':
    line = line.split(': ')
    if line[0] == 'Add':
        animal_info = line[1].split('-')
        animal, needed_food, area = animal_info[0], int(animal_info[1]), animal_info[2]
        if animal not in animals:
            animals[animal] = {'food': needed_food, 'area': area}
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
        else:
            animals[animal]['food'] += needed_food
    elif line[0] == 'Feed':
        animal_info = line[1].split('-')
        animal, food = animal_info[0], int(animal_info[1])
        if animal in animals:
            animals[animal]['food'] -= food
            if animals[animal]['food'] <= 0:
                areas[animals[animal]['area']] -= 1
                del animals[animal]
                print(f'{animal} was successfully fed')
    line = input()

print('Animals:')
for animal in animals:
    print(f' {animal} -> {animals[animal]["food"]}g')

print('Areas with hungry animals:')
for area, count in areas.items():
    if count > 0:
        print(f' {area}: {count}')

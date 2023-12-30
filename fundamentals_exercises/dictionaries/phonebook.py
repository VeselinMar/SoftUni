people_number = input()
phonebook = {}
while '-' in people_number:
    edited = people_number.split('-')
    name, number = edited[0], edited[1]
    phonebook[name] = number
    people_number = input()

for _ in range(int(people_number)):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')

legendary_item = {'Shadowmourne': 0, 'Valanyr': 0, 'Dragonwrath': 0}
junk = {}

while True:
    line = input().split()
    quantity, material = int(line[0]), line[1].lower()

    if material == "shards":
        legendary_item['Shadowmourne'] += quantity
        if legendary_item['Shadowmourne'] >= 250:
            print('Shadowmourne obtained!')
            print('\n'.join(f'{key}: {val}' for key, val in legendary_item.items() if key != 'Shadowmourne'))
            break

    elif material == 'fragments':
        legendary_item['Valanyr'] += quantity
        if legendary_item['Valanyr'] >= 250:
            print('Valanyr obtained!')
            print('\n'.join(f'{key}: {val}' for key, val in legendary_item.items() if key != 'Valanyr'))
            break

    elif material == 'motes':
        legendary_item['Dragonwrath'] += quantity
        if legendary_item['Dragonwrath'] >= 250:
            print('Dragonwrath obtained!')
            print('\n'.join(f'{key}: {val}' for key, val in legendary_item.items() if key != 'Dragonwrath'))
            break

    else:
        if material in junk:
            junk[material] += quantity
        else:
            junk[material] = quantity

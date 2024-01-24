from collections import deque

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted = []

material_values = [int(value) for value in input().split()]
magic_values = deque(int(value) for value in input().split())

while material_values and magic_values:
    material = material_values.pop() if magic_values[0] or not material_values[-1] else 0
    magic = magic_values.popleft() if material or not magic_values[0] else 0

    if not magic:
        continue

    product = material * magic

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        material_values.append(material + magic)
    elif product > 0:
        material_values.append(material + 15)


if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if material_values or magic_values:
    if material_values:
        print(f"Materials left: {', '.join(str(x) for x in material_values[::-1])}")
    if magic_values:
        print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]

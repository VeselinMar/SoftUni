from collections import deque

textiles = deque([int(item) for item in input().split()])
medicament = [int(item) for item in input().split()]

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

created_items = {}
while textiles and medicament:
    textile = textiles.popleft()
    medicament_item = medicament[-1]
    result = textile + medicament_item
    if result in healing_items.keys():
        if healing_items[result] not in created_items:
            created_items[healing_items[result]] = 1
        else:
            created_items[healing_items[result]] += 1
        medicament.pop()
    elif result > 100:
        if healing_items[100] not in created_items:
            created_items[healing_items[100]] = 1
        else:
            created_items[healing_items[100]] += 1
        medicament.pop()
        medicament[-1] += result - 100
    else:
        medicament[-1] += 10

if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicament:
    print("Medicaments are empty.")

if created_items:
    for item, value in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item} - {value}")

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicament))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

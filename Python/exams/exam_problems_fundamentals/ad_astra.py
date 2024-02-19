import re

line = input()
calories = 0

pattern = (r'#([A-Za-z ]+)#([0123][0-9]\/[01][0-9]\/[0-9]{2})#([0-9]+)#'
           r'|\|([A-Za-z ]+)\|([0123][0-9]\/[01][0-9]\/[0-9]{2})\|([0-9]+)\|')

matches = list(re.finditer(pattern, line))  # make the iter reusable by storing inside a list

for match in matches:
    if match.group(3) is None:
        calories += int(match.group(6))
    else:
        calories += int(match.group(3))
print(f"You have food to last you for: {int(calories / 2000)} days!")

for match in matches:
    if match.group(3) is None:
        print(f"Item: {match.group(4)}, Best before: {match.group(5)}, Nutrition: {match.group(6)}")
    else:
        print(f"Item: {match.group(1)}, Best before: {match.group(2)}, Nutrition: {match.group(3)}")

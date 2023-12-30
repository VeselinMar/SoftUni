line = input()

char_count = {}

for char in line:
    if char == ' ':
        continue
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char} -> {count}")

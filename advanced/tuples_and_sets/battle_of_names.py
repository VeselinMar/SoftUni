N = int(input())

odd_numbers = set()
even_numbers = set()
for row in range(1, N + 1):
    name = input()
    name_sum = 0
    for letter in name:
        name_sum += ord(letter)
    name_value = name_sum // row
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)

if odd_sum == even_sum:
    result = odd_numbers | even_numbers
elif odd_sum > even_sum:
    result = odd_numbers - even_numbers
else:
    result = odd_numbers ^ even_numbers

print(', '.join(map(str, result)))

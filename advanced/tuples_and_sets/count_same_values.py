numbers = tuple(float(number) for number in input().split(' '))

seen = []
for number in numbers:
    if number not in seen:
        print(f'{number:.1f} - {numbers.count(number)} times')
        seen.append(number)

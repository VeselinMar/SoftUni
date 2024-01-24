from collections import deque

chocolates = deque(int(item) for item in input().split(','))
cups_of_milk = deque(int(item) for item in input().split(','))


shakes = 0

while chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
    else:
        if chocolate == milk:
            shakes += 1
            if shakes == 5:
                break
        else:
            cups_of_milk.append(milk)
            chocolate -= 5
            chocolates.append(chocolate)

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end='')
    print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")

if cups_of_milk:
    print("Milk: ", end='')
    print(*cups_of_milk, sep=', ')
else:
    print("Milk: empty")

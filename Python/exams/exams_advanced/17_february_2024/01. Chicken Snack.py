from collections import deque

amount_of_money = [int(money) for money in input().split()]
prices_deque = deque([int(price) for price in input().split()])

food_bought = 0
while amount_of_money and prices_deque:
    money = amount_of_money.pop()
    price = prices_deque.popleft()

    if money == price:
        food_bought += 1

    elif money > price:
        food_bought += 1
        if amount_of_money:
            amount_of_money[-1] += money - price

if food_bought:
    if food_bought >= 4:
        print(f"Gluttony of the day! Henry ate {food_bought} foods.")
    elif food_bought == 1:
        print(f"Henry ate: {food_bought} food.")
    else:
        print(f"Henry ate: {food_bought} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")

film_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_cinema = int(input())

total_income = number_of_days * number_of_tickets * price_per_ticket
profit = total_income - (total_income * (percent_for_cinema / 100))

print(f"The profit from the movie {film_name} is {profit:.2f} lv.")

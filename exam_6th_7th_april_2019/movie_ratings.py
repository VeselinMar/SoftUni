number_of_films = int(input())

rating_total = 0
lowest_rating = 11
film_lowest = ''
highest_rating = 0
film_highest = ''
for films in range(number_of_films):
    film_name = input()
    film_rating = float(input())
    rating_total += film_rating

    if film_rating > highest_rating:
        highest_rating = film_rating
        film_highest = film_name

    elif film_rating < lowest_rating:
        lowest_rating = film_rating
        film_lowest = film_name

average_rating = rating_total / number_of_films

print(f"{film_highest} is with highest rating: {highest_rating:.1f}")
print(f"{film_lowest} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

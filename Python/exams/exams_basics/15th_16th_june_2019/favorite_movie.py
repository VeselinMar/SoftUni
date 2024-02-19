from curses.ascii import isupper, isalpha

number_of_films = 0
best_film = ''
best_score = 0
film_score = 0
while True:
    film_score = 0
    film = input()
    if film == 'STOP':
        break

    number_of_films += 1
    for letter in film:
        film_score += ord(letter)
        if isalpha(letter):
            if not isupper(letter):
                film_score -= 2 * len(film)
            elif isupper(letter):
                film_score -= len(film)
        else:
            pass

    if film_score > best_score:
        best_score = film_score
        best_film = film

    if number_of_films == 7:
        print(f"The limit is reached.")
        break

print(f"The best movie for you is {best_film} with {best_score} ASCII sum.")

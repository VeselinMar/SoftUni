from collections import defaultdict


def movie_organizer(*args):
    catalogue = defaultdict(list)
    for movie, movie_genre in args:
        catalogue[movie_genre].append(movie)

    sorted_catalogue = sorted(catalogue.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for genre, movies in sorted_catalogue:
        result.append(f"{genre} - {len(movies)}")
        result.extend(f"* {movie}" for movie in sorted(movies))

    return '\n'.join(result)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

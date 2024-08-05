import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Actor, Movie, Director
from django.db.models import Q, Count, Avg, F


# Create queries within functions


def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name and search_nationality:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(nationality__icontains=search_nationality)
        ).order_by('full_name')

    elif search_name:
        directors = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')

    elif search_nationality:
        directors = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')

    else:
        return ''

    result = []
    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality},"
                      f" experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director() -> str:
    top_director = Director.objects.get_directors_by_movies_count().first()

    if top_director is None:
        return ''

    return f"Top Director: {top_director.full_name}, movies: {top_director.movie_count}."


def get_top_actor() -> str:
    top_actor = (
        Actor.objects
        .annotate(movie_count=Count('starring_in'))
        .order_by('-movie_count', 'full_name')
        .first()
    )

    if not top_actor:
        return ''

    movies = top_actor.starring_in.all()

    if not movies:
        return ''

    movie_titles = [movie.title for movie in movies]
    avg_rating = movies.aggregate(Avg('rating'))['rating__avg']

    return (f"Top Actor: {top_actor.full_name},"
            f" starring in movies: {', '.join(movie_titles)},"
            f" movies average rating: {avg_rating:.1f}")


def get_actors_by_movies_count() -> str:
    actors = (
        Actor.objects
        .annotate(participations=Count('movies'))
        .order_by('-participations', 'full_name')
    )

    movies = Movie.objects.all()

    if not actors.exists() or not movies.exists():
        return ''

    best_actors = actors[:3]

    result = []

    for actor in best_actors:
        result.append(f"{actor.full_name}, participated in {actor.participations} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie() -> str:
    top_movie = (
        Movie.objects
        .select_related('starring_actor')
        .prefetch_related('actors')
        .filter(is_awarded=True)
        .order_by('-rating', 'title')
        .first()
    )

    if top_movie is None:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"

    participating_actors = top_movie.actors.order_by("full_name").values_list('full_name', flat=True)
    cast = ', '.join(participating_actors)

    return (f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {cast}.")


def increase_rating():
    classic_movies = Movie.objects.filter(Q(is_classic=True) & Q(rating__lt=10.0)).all()

    updated_count = classic_movies.count()

    if not updated_count:
        return "No ratings increased."

    classic_movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_count} movies."

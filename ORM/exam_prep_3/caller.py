import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg


# Create queries within functions


def get_authors(search_name=None, search_email=None) -> str:
    # if both arguments = None
    if not search_name and not search_email:
        return ''

    # if one of both = None
    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_email:
        query &= Q(email__icontains=search_email)

    # Fetch authors based on the constructed query
    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors.exists():
        return ''

    result = [(f"Author: {author.full_name},"
               f" email: {author.email},"
               f" status: {'Banned' if author.is_banned else 'Not Banned'}")
              for author in authors]

    return '\n'.join(result)


def get_top_publisher() -> str:
    author = (Author.objects.
              annotate(publications=Count('article'))
              .order_by('-publications', 'email')
              .first())

    if not author or author.publications == 0:
        return ''

    return f"Top Author: {author.full_name} with {author.publications} published articles."


def get_top_reviewer() -> str:
    author = (Author
              .objects
              .annotate(reviews=Count('review'))
              .order_by('-reviews', 'email')
              .first()
              )

    if not author or author.reviews == 0:
        return ''

    return f"Top Reviewer: {author.full_name} with {author.reviews} published reviews."


def get_latest_article() -> str:
    last_article = (Article.objects
                    .annotate(reviews_num=Count('review'))
                    .order_by('-published_on')
                    .prefetch_related('authors__article_set', 'review_set__author__article_set')
                    .first())

    if not last_article:
        return ''

    authors = last_article.authors.order_by('full_name').all()
    authors_names = ', '.join(author.full_name for author in authors)

    avg_reviews_rating = (last_article.review_set.aggregate(Avg('rating'))['rating__avg']
                          or 0)

    return (f"The latest article is: {last_article.title}. "
            f"Authors: {authors_names}. "
            f"Reviewed: {last_article.reviews_num} times. "
            f"Average Rating: {avg_reviews_rating:.2f}.")


def get_top_rated_article() -> str:
    articles_with_ratings = (Article.objects
                             .annotate(avg_rating=Avg('review__rating'), num_reviews=Count('review'))
                             .order_by('-avg_rating', 'title')
                             .first())

    if not articles_with_ratings or articles_with_ratings.num_reviews == 0:
        return ''

    avg_rating = articles_with_ratings.avg_rating
    return (f"The top-rated article is: {articles_with_ratings.title}, "
            f"with an average rating of {avg_rating:.2f}, reviewed {articles_with_ratings.num_reviews} times.")


def ban_author(email=None) -> str:
    if email is None:
        return 'No authors banned.'

    try:
        # Retrieve the author with the given email and count their reviews
        to_ban = Author.objects.annotate(num_reviews=Count('review')).get(email=email)

        # Get the number of reviews
        num_reviews = to_ban.num_reviews

        # Delete all reviews associated with the author
        Review.objects.filter(author=to_ban).delete()

        # Update the author’s banned status
        to_ban.is_banned = True
        to_ban.save()

        return f"Author: {to_ban.full_name} is banned! {num_reviews} reviews deleted."

    except Author.DoesNotExist:
        return 'No authors banned.'

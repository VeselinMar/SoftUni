import os


import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


from django.db.models import Q, Count
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions


def get_tennis_players(search_name=None, search_country=None):
    if not search_country and not search_name:
        return ''
    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_country:
        query &= Q(country__icontains=search_country)

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players.exists():
        return ''

    result = [f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}"
              for player in players]

    return '\n'.join(result)


def get_top_tennis_player():
    top_player = (TennisPlayer.objects
                  .annotate(num_of_wins=Count('tournament_winner'))
                  .order_by('-num_of_wins', 'full_name')
                  .first())

    if not top_player:
        return ''

    return f"Top Tennis Player: {top_player.full_name} with {top_player.num_of_wins} wins."


def get_tennis_player_by_matches_count():
    active_player = (TennisPlayer.objects
                     .annotate(num_of_matches=Count('match'))
                     .order_by('-num_of_matches', 'ranking')
                     .first())

    if not active_player or active_player.num_of_matches == 0:
        return ''

    return f"Tennis Player: {active_player.full_name} with {active_player.num_of_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''

    tournaments = (Tournament.objects
                   .annotate(num_matches=Count('match'))
                   .filter(surface_type__icontains=surface)
                   .order_by('-start_date'))

    if not tournaments.exists():
        return ''

    result = [f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}"
              for t in tournaments]

    return '\n'.join(result)


def get_latest_match_info():
    last_match = (Match.objects
                  .prefetch_related('players', 'tournament')
                  .order_by('-date_played', '-id')
                  .first())

    if not last_match:
        return ''

    players = list(last_match.players.all())

    return (f"Latest match played on: {last_match.date_played},"
            f" tournament: {last_match.tournament.name},"
            f" score: {last_match.score},"
            f" players: {players[0].full_name} vs {players[1].full_name},"
            f" winner: {last_match.winner.full_name if last_match.winner else 'TBA'},"
            f" summary: {last_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return 'No matches found.'

    matches = Match.objects.filter(tournament__name__exact=tournament_name).order_by('-date_played').all()

    if not matches.exists():
        return 'No matches found.'

    result = [(f"Match played on: {match.date_played},"
               f" score: {match.score},"
               f" winner: {match.winner.full_name if match.winner else 'TBA'}")
              for match in matches]

    return '\n'.join(result)

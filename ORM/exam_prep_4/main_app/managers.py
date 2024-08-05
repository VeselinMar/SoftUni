from django.db import models
from django.db.models import Count


class TennisPlayerManager(models.Manager):
    def get_tennis_players_by_wins_count(self):
        return self.annotate(num_of_wins=Count('tournament_winner')).order_by('-num_of_wins', 'full_name')

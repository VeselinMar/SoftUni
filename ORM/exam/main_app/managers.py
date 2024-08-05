from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return (self
                .annotate(num_of_missions=Count('missions'))
                .order_by('-num_of_missions', 'phone_number')
                .all()
                )

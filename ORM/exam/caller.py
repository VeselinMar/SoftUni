import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions


from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, Sum, F, Avg, Case, When, IntegerField


def get_astronauts(search_string=None) -> str:
    if search_string is None:
        return ''

    astronauts = (Astronaut
                  .objects
                  .filter(Q(name__icontains=search_string) | Q(phone_number__icontains=search_string))
                  .order_by('name'))

    if not astronauts.exists():
        return ''

    result = [
        f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}"
        for a in astronauts
    ]

    return '\n'.join(result)


def get_top_astronaut() -> str:
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    result = (f"Top Astronaut: {top_astronaut.name} with {top_astronaut.num_of_missions} missions."
              if top_astronaut and top_astronaut.num_of_missions > 0 else "No data.")

    return result


def get_top_commander() -> str:
    top_commander = (Astronaut.objects
                     .annotate(num_of_missions=Count('missions_as_commander'))
                     .order_by('-num_of_missions', 'phone_number')
                     .first())

    if not top_commander or top_commander.num_of_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_missions} commanded missions."


def get_last_completed_mission() -> str:
    last_mission = (Mission.objects
                    .filter(status='Completed')
                    .select_related('commander', 'spacecraft')
                    .prefetch_related('astronauts')
                    .order_by('-launch_date')
                    .first())

    if not last_mission:
        return 'No data.'

    astronaut_names = last_mission.astronauts.order_by('name').values_list('name', flat=True)

    commander_name = last_mission.commander.name if last_mission.commander else 'TBA'

    total_spacewalks = last_mission.astronauts.aggregate(Sum('spacewalks'))['spacewalks__sum'] or 0

    return (f"The last completed mission is: {last_mission.name}."
            f" Commander: {commander_name}."
            f" Astronauts: {', '.join(name for name in astronaut_names)}."
            f" Spacecraft: {last_mission.spacecraft.name}."
            f" Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft() -> str:
    most_used_spacecraft = (Spacecraft.objects
                            .annotate(num_of_missions=Count('mission'))
                            .order_by('-num_of_missions', 'name')
                            .first())

    completed_missions = Mission.objects.filter(status='Completed').all()

    if not completed_missions.exists() or not most_used_spacecraft:
        return 'No data.'

    num_of_astronauts = (most_used_spacecraft.mission_set
                         .prefetch_related('astronauts')
                         .aggregate(num_astronauts=Count('astronauts', distinct=True))['num_astronauts'] or 0)

    return (f"The most used spacecraft is: {most_used_spacecraft.name},"
            f" manufactured by {most_used_spacecraft.manufacturer},"
            f" used in {most_used_spacecraft.num_of_missions} missions,"
            f" astronauts on missions: {num_of_astronauts}.")


def decrease_spacecrafts_weight():
    spacecrafts_to_update = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    ids_to_update = spacecrafts_to_update.values_list('id', flat=True)
    num_of_spacecrafts_affected = len(ids_to_update)

    if num_of_spacecrafts_affected == 0:
        return 'No changes in weight.'

    Spacecraft.objects.filter(id__in=ids_to_update).update(
        weight=F('weight') - 200.0
    )

    Spacecraft.objects.filter(weight__lt=0.0).update(weight=0.0)

    avg_weight_subquery = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']
    avg_weight = avg_weight_subquery if avg_weight_subquery is not None else 0.0

    result = (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
              f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")

    return result


print(decrease_spacecrafts_weight())

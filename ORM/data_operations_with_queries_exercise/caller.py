import os
from decimal import Decimal

import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions


def create_pet(name: str, species: str):
    pet = Pet(
        name=name,
        species=species,
    )
    pet.save()
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    artifact.save()
    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.age > 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    artifacts = Artifact.objects.all()
    for artifact in artifacts:
        artifact.delete()


def show_all_locations():
    # Fetch all Location objects sorted by id in descending order
    locations = Location.objects.all().order_by('-id')

    # Create a list to hold formatted location information
    locations_info = []

    # Iterate through each location and format its information
    for location in locations:
        locations_info.append(f"{location.name} has a population of {location.population}!")

    # Join the list into a single string with each location's info on a new line
    return '\n'.join(locations_info)


def new_capital():
    # use objects.first to get first object
    location_to_be_capital = Location.objects.first()
    # change the first object's capital boolean value to True and save
    if location_to_be_capital:
        location_to_be_capital.is_capital = True
        location_to_be_capital.save()


def get_capitals():
    # Filter locations where is_capital is True and project only the name field
    capitals = Location.objects.filter(is_capital=True).values('name')
    return capitals


def delete_first_location():
    # use objects.first to get first object
    location_to_be_deleted = Location.objects.first()
    # delete the first object
    if location_to_be_deleted:
        location_to_be_deleted.delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        # Calculate the sum of digits in the year using a generator expression
        year_digits_sum = sum(int(digit) for digit in str(car.year))

        # Calculate the discount based on the sum of the year digits
        discount_percent = Decimal(year_digits_sum)

        # Calculate the discount amount
        discount_amount = car.price * (discount_percent / Decimal(100))

        # Update the price with discount in memory
        car.price_with_discount = car.price - discount_amount

    # Perform bulk update of all cars
    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    # Fetch a query set of cars created after 2020 containing model and price with discount and return it
    recent_cars = Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')
    return recent_cars


def delete_last_car():
    # Fetch last car using objects.last() and delete it
    last_car = Car.objects.last()
    if last_car:
        last_car.delete()


def show_unfinished_tasks():
    # Fetch all unfinished tasks using objects.filter
    unfinished_tasks = Task.objects.filter(is_finished=False)
    result = []
    for task in unfinished_tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")
    # Return unfinished tasks' information each task on new line
    return '\n'.join(result)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 == 1:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    # Fetch all tasks with the given title
    tasks = Task.objects.filter(title=task_title)

    # Calculate encoded text
    encoded_text = ''.join(chr(ord(char) - 3) for char in text)

    # Update each task description with encoded text
    for task in tasks:
        task.description = encoded_text
        task.save()


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]

    return '\n'.join(even_deluxe_rooms)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    if first_room:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if last_room and not last_room.is_reserved:
        last_room.delete()


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty'
    )


def fuse_characters(first_character: Character, second_character: Character):
    fusion_name = first_character.name + ' ' + second_character.name
    class_name = 'Fusion'
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ['Mage', 'Scout']:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    characters = Character.objects.all()

    for c in characters:
        c.dexterity = 30

    Character.objects.bulk_update(characters, ['dexterity'])


def grand_intelligence():
    characters = Character.objects.all()

    for c in characters:
        c.intelligence = 40

    Character.objects.bulk_update(characters, ['intelligence'])


def grand_strength():
    characters = Character.objects.all()

    for c in characters:
        c.strength = 50

    Character.objects.bulk_update(characters, ['strength'])


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()


complete_odd_tasks()
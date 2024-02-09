def accommodate_new_pets(capacity: int, max_weight: float,  *args):
    accommodated = {}
    overbooked = False
    if args:
        for arg in args:
            if capacity == 0:
                overbooked = True
                break
            pet_type, pet_weight = arg
            if pet_weight > max_weight:
                continue
            else:
                if pet_type not in accommodated:
                    accommodated[pet_type] = 1
                    capacity -= 1
                else:
                    accommodated[pet_type] += 1
                    capacity -= 1

    sorted_pets = sorted(accommodated.items())
    accommodated_pets_string = '\n'.join([f"{pet}: {quantity}" for pet, quantity in sorted_pets])

    if not overbooked:
        return (f"All pets are accommodated! Available capacity: {capacity}.\n"
                f"Accommodated pets:\n"
                f"{accommodated_pets_string}")
    else:
        return (f"You did not manage to accommodate all pets!\n"
                f"Accommodated pets:\n"
                f"{accommodated_pets_string}")


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.0),
    ("parrot", 0.8),
    ("cat", 3.1),
    ("deer", 9.0),
    ("ape", 2.0),
    ("bat", 1.0),
    ("elephant", 8.0),
    ("fly", 0.1),
    ("goat", 6.0),
    ("zebra", 9.0),
    ("akula", 2.9)
))

def add_stop(list_of_countries: str, index: int, string: str):
    if len(list_of_countries) >= index:
        first_half = list_of_countries[0:index] + string
        second_half = list_of_countries[index::]
        return first_half + second_half
    else:
        return list_of_countries


def remove_stop(list_of_countries: str, start: int, end: int):
    if len(list_of_countries) >= start and len(list_of_countries) >= end:
        first_half = list_of_countries[0:start]
        second_half = list_of_countries[end + 1:]
        return first_half + second_half
    else:
        return list_of_countries


def switch(list_of_countries: str, old: str, new: str):
    if old in list_of_countries:
        list_of_countries = list_of_countries.replace(old, new)
    return list_of_countries


destinations = input()

command = input()
while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        destinations = add_stop(destinations, index, string)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        destinations = remove_stop(destinations, start_index, end_index)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        destinations = switch(destinations, old_string, new_string)
    print(destinations)
    command = input()

print(f"Ready for world tour! Planned stops: {destinations}")

import sys

name_actor = input()
points_academy = float(input())
number_of_jury = int(input())
points_from_jury = 0
points_total = points_academy
for jury in range(number_of_jury):

    name_jury_member = input()
    points_jury_member = float(input())
    points_from_jury = (points_jury_member * len(name_jury_member)) / 2
    points_total += points_from_jury

    if points_total > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_total:.1f}!")
        sys.exit()

print(f"Sorry, {name_actor} you need {1250.5 - points_total:.1f} more!")

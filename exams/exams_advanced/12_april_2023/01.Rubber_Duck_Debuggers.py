from collections import deque


def duck_assignment(result):
    if 0 <= result <= 60:
        return "Darth Vader Ducky"
    elif 61 <= result <= 120:
        return "Thor Ducky"
    elif 121 <= result <= 180:
        return "Big Blue Rubber Ducky"
    elif 181 <= result <= 240:
        return "Small Yellow Rubber Ducky"
    else:
        return None


time_pro_task = deque([int(value) for value in input().split()])
tasks = [int(value) for value in input().split()]

ducks = []
while time_pro_task and tasks:
    time_for_task = time_pro_task.popleft()
    task = tasks.pop()
    mult_result = time_for_task * task
    duck = duck_assignment(mult_result)
    if duck:
        ducks.append(duck)
    else:
        time_pro_task.append(time_for_task)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks.count('Darth Vader Ducky')}")
print(f"Thor Ducky: {ducks.count('Thor Ducky')}")
print(f"Big Blue Rubber Ducky: {ducks.count('Big Blue Rubber Ducky')}")
print(f"Small Yellow Rubber Ducky: {ducks.count('Small Yellow Rubber Ducky')}")

import math

series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_duration_raw = float(input())

advertisement_break = episode_duration_raw * 0.2
time = number_of_seasons * number_of_episodes * (episode_duration_raw + advertisement_break) + 10 * number_of_seasons

print(f"Total time needed to watch the {series_name} series is {math.floor(time)} minutes.")

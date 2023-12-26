shooting_time = int(input())
number_of_scenes = int(input())
scene_duration = int(input())

terrain_preparation = shooting_time * 0.15
time_needed = number_of_scenes * scene_duration + terrain_preparation

if shooting_time >= time_needed:
    print(f"You managed to finish the movie on time! You have {round(shooting_time - time_needed)} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {round(time_needed - shooting_time)} minutes.")

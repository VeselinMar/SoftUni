from collections import deque

food_portions = [int(portion) for portion in input().split(', ')]
daily_stamina = deque([int(stamina) for stamina in input().split(', ')])

to_climb = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])
conquered_peaks = []

bonus = 0
for _ in range(7):
    food = food_portions.pop()
    stamina = daily_stamina.popleft()
    result = food + stamina
    if result >= 80 + bonus:
        peak = to_climb.popleft()
        conquered_peaks.append(peak)
        if len(conquered_peaks) != 3:
            bonus += 10
        else:
            bonus = -20
        if not to_climb:
            break

if not to_climb:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)

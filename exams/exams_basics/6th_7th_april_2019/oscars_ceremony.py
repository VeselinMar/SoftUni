rent_hall = int(input())

statues = rent_hall - rent_hall * 0.3
catering = statues - statues * 0.15
sound = catering - catering * 0.5

print(f"{rent_hall + statues + catering + sound:.2f}")

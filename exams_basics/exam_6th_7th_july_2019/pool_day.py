import math

people_number = int(input())
entrance_fee = float(input())
bed_fee = float(input())
umbrella_fee = float(input())

total_entrance = entrance_fee * people_number
total_bed = bed_fee * math.ceil(people_number * 0.75)
total_umbrellas = umbrella_fee * math.ceil(people_number * 0.5)
total = total_entrance + total_umbrellas + total_bed

print(f'{total:.2f} lv.')

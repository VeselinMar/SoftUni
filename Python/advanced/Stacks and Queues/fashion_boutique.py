# convert input to list of integers
box_of_clothes = list(map(int, input().split()))
# define amount of items that fit on a rack
capacity_of_rack = int(input())
# we need at least 1 rack
racks_needed = 1
# save remaining rack capacity in a variable
remaining_rack_capacity = capacity_of_rack
while box_of_clothes:
    item = box_of_clothes.pop()
    # if enough place on rack -> reduce place on rack
    if remaining_rack_capacity >= item:
        remaining_rack_capacity -= item
    # else take new rack
    else:
        remaining_rack_capacity = capacity_of_rack
        remaining_rack_capacity -= item
        racks_needed += 1
# print racks needed
print(racks_needed)

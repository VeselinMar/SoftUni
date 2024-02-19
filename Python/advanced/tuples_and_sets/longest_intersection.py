N = int(input())

longest = list()
for _ in range(N):
    range_one, range_two = input().split('-')
    ro_start, ro_end = range_one.split(',')
    rt_start, rt_end = range_two.split(',')
    first_set = set()
    second_set = set()
    for num in range(int(ro_start), int(ro_end) + 1):
        first_set.add(num)
    for num in range(int(rt_start), int(rt_end) + 1):
        second_set.add(num)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = list(intersection)

print(f'Longest intersection is {longest} with length {len(longest)}')

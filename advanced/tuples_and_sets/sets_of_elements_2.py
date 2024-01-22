n, m = [int(x) for x in input().split()]  # "4 3" -> ["4", "3"] -> [4, 3]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set.intersection(second_set), sep="\n")

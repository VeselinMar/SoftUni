from collections import deque

initial_fuel = [int(num) for num in input().split()]
additional_consumption_index = deque([int(num) for num in input().split()])
fuel_needed = deque([int(num) for num in input().split()])

failed = False
count = 0

while initial_fuel and additional_consumption_index and fuel_needed:
    result = initial_fuel.pop() - additional_consumption_index.popleft()
    if result >= fuel_needed.popleft():
        count += 1
        print(f"John has reached: Altitude {count}")
    else:
        failed = True
        print(f"John did not reach: Altitude {count + 1}")
        break

if failed and not count:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif failed:
    print("John failed to reach the top.\nReached altitudes: ", end='')

    altitudes = []
    for i in range(1, count+1):
        altitudes.append(f'Altitude {i}')
    print(*altitudes, sep=', ')

else:
    print("John has reached all the altitudes and managed to reach the top!")

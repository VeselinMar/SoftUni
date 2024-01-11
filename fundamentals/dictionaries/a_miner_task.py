line = input()

resources = {}
while line != 'stop':
    value = int(input())
    if line not in resources:
        resources[line] = value
    else:
        resources[line] += value
    line = input()

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')

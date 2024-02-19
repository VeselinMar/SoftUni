from collections import deque

tools = deque([int(value) for value in input().split()])
substances = [int(value) for value in input().split()]
challenges = [int(value) for value in input().split()]

fail = True
while challenges:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        if substance > 1:
            substances.append(substance - 1)
    if not challenges:
        fail = False
        break
    if not tools or not substances:
        break

if fail:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print('Tools: ', end='')
    print(*tools, sep=', ')
if substances:
    print('Substances: ', end='')
    print(*substances, sep=', ')
if challenges:
    print('Challenges: ', end='')
    print(*challenges, sep=', ')

# import deque from collections
from collections import deque
# initiate main stack
stack = deque()
# initiate control stack
track_stack = deque()

n = int(input())

for _ in range(n):
    command = input()
    # check if there are any elements in stack before trying to manipulate them
    if stack:
        # if 2 pop last element in stack and remove the element from control stack if needed
        if command == '2':
            number = int(stack.pop())
            if track_stack[0] == number:
                track_stack.popleft()
            elif track_stack[-1] == number:
                track_stack.pop()
        # if 3 print max element
        elif command == '3':
            print(track_stack[-1])
        # if 4 print min element
        elif command == '4':
            print(track_stack[0])
    # add element to stack and track stack
    if len(command) > 1:
        command = command.split()
        number = command[1]
        stack.append(number)
        if not track_stack:
            track_stack.append(int(number))
        else:
            if int(number) < track_stack[0]:
                track_stack.appendleft(int(number))
            elif int(number) > track_stack[-1]:
                track_stack.append(int(number))
# reverse stack
stack.reverse()
# print out the stack elements from bottom to top
print(', '.join(stack))

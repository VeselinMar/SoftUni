# convert input into a list
line = list(input())
# save starting indexes into a stack
parentheses_open = []
for index in range(len(line)):
    if line[index] == '(':
        parentheses_open.append(index)
    elif line[index] == ')':
        # take the last index from the stack and use it to print the result
        opening = parentheses_open.pop()
        print(''.join((line[opening: index + 1])))

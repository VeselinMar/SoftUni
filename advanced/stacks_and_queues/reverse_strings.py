# convert input to a list
line = list(input())
# use list as a stack
while line:
    print(line.pop(), end='')

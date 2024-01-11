# split input into a list
numbers = input().split()
# print elements in reverse order on one line separated by an interval
for _ in range(len(numbers)):
    number = numbers.pop()
    print(number, end=' ')

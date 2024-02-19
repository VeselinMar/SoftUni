first_sequence = {int(number) for number in input().split()}
second_sequence = {int(number) for number in input().split()}
N = int(input())

for _ in range(N):
    line = input().split()
    if len(line) == 2:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
    else:
        command, sequence, numbers = line[0], line[1], {int(num) for num in line if num.isdigit()}
        if command == 'Add':
            if sequence == 'First':
                first_sequence = first_sequence.union(numbers)
            elif sequence == 'Second':
                second_sequence = second_sequence.union(numbers)
        elif command == 'Remove':
            if sequence == 'First':
                first_sequence.difference_update(numbers)
            elif sequence == 'Second':
                second_sequence.difference_update(numbers)

print(* sorted(first_sequence), sep=', ')
print(* sorted(second_sequence), sep=', ')

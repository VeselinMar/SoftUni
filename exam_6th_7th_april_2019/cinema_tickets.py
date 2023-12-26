total_tickets = 0
student = 0
standard = 0
kid = 0
while True:
    film_name = input()
    if film_name == 'Finish':
        break
    free_seats = int(input())
    tickets = 0
    for film in range(1, free_seats + 1):
        ticket = input()
        if ticket == 'End':
            break
        total_tickets += 1
        tickets += 1
        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        elif ticket == 'kid':
            kid += 1

    print(f'{film_name} - {(tickets / free_seats) * 100:.2f}% full.')

print(f'Total tickets: {total_tickets}')
print(f'{(student / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid / total_tickets) * 100:.2f}% kids tickets.')

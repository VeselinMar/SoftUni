companies = {}
command = input()
while command != 'End':
    f_command = command.split(' -> ')
    company, employee = f_command[0], f_command[1]
    if company not in companies:
        companies[company] = [employee]
    else:
        if employee not in companies[company]:
            companies[company].append(employee)

    command = input()

for company, employee in companies.items():
    print(f'{company}')
    for person in employee:
        print(f'-- {person}')

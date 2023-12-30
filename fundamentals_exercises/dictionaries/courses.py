courses = {}
command = input()
while command != 'end':
    split = command.split(' : ')
    course_name, student_name = split[0], split[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name] += [student_name]
    command = input()

for course, name in courses.items():
    print(f'{course}: {len(courses[course])}')
    for student in courses[course]:
        print(f'-- {student}')

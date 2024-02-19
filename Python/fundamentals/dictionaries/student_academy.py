pair_of_rows = int(input())
grades = {}
for _ in range(pair_of_rows):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

names_to_delete = []
for name, grade_list in grades.items():
    avg_grade = sum(grade_list) / len(grade_list)
    if avg_grade < 4.50:
        names_to_delete.append(name)
    else:
        grades[name] = avg_grade
for name in names_to_delete:
    grades.pop(name)

for name, grade in grades.items():
    print(f'{name} -> {grade:.2f}')

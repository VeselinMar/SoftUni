n = int(input())

student_record = {}

for _ in range(n):
    student, grade_as_string = input().split()
    grade = float(grade_as_string)

    if student not in student_record:
        student_record[student] = []
    student_record[student].append(grade)

for student, grade in student_record.items():
    avg_grade = sum(grade) / len(grade)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grade])}"
    print(f'{student} -> {formatted_grades} (avg: {avg_grade:.2f})')

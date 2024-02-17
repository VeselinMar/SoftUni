def students_credits(*strings):
    test_stats = {}
    for string in strings:
        string_to_list = string.split('-')
        course_name, course_credits, max_test_points, test_points = string_to_list
        result = (int(test_points) / int(max_test_points)) * int(course_credits)
        test_stats[course_name] = result

    total_score = sum(test_stats.values())
    return_string = ''
    if total_score >= 240:
        return_string += f"Diyan gets a diploma with {total_score:.1f} credits.\n"
    else:
        return_string += f"Diyan needs {240 - total_score:.1f} credits more for a diploma.\n"
    for course_name, credit in sorted(test_stats.items(), key=lambda x: -x[1]):
        return_string += f"{course_name} - {credit:.1f}\n"

    return return_string


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
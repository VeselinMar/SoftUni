def gather_credits(credits_needed, *args):
    total_credits = 0
    courses = []
    for course, credit_points in args:
        if total_credits >= credits_needed:
            break
        if course in courses:
            continue
        courses.append(course)
        total_credits += credit_points

    if total_credits >= credits_needed:
        result = f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(courses))}"
    else:
        result = (f"You need to enroll in more courses! You have to gather"
                  f" {credits_needed - total_credits} credits more.")

    return result


print(gather_credits(
    60,
    ("Basics", 27),
    ("Basics", 60),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

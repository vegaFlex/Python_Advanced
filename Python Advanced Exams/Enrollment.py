def gather_credits(needed_credits, *args):
    enrolled_courses = []
    gathered_credits = 0

    for course_name, course_credits in args:
        if gathered_credits >= needed_credits:
            break

        if course_name in enrolled_courses:
            continue

        enrolled_courses.append(course_name)
        gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"

    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."




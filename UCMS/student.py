import database

#Allows students to search for classes according to class name
def course_search():

    while True:

        search_term = input("Enter course name to search "
                            "(or enter X to exit): ").lower()

        if search_term == "x":
            return

        matches = []

        for course_id, course in database.courses.items():
            if search_term in course["course_name"].lower():
                matches.append((course_id, course))

        if len(matches) == 0:
            print("No classes found.")
            continue

        print("\nCourses found:")
        for course_id, course in matches:
            available_seats = (course["max_seats"]
                               - len(course["students"]))

            print(
                f"Course: {course['course_name']} | "
                f"Course ID: {course['course_id']} | "
                f"Section: {course['section_number']} | "
                f"Seats Available: {available_seats}")

        return

#Allows students to enroll in courses according to section key
def course_enroll(student_id):

    while True:

        selected_course = input(
            "Enter section key "
            "(example COP101-001): ")

        if selected_course not in database.courses:
            print("Invalid Course ID")
            continue

        course = database.courses[selected_course]

        if student_id in course["students"]:
            print("You are already enrolled in this course.")
            continue

        available_seats = (course["max_seats"] - len(course["students"]))

        if available_seats <= 0:
            print("Course is full.")
            continue

        course["students"].append(student_id)

        print("Enrollment successful")

        return

#Shows remaining courses needed to complete your degree requirements
#and calculates your gpa
def academic_tracker(student_id):
    major = database.users[student_id]["major"]

    required_courses = (
        database.degree_requirements[major]
    )

    completed_courses = set()

    for course_id, course in database.courses.items():

        if student_id in course["grades"]:

            letter_grade = course ["grades"][student_id]["grade"]

            if letter_grade != "F" and letter_grade != "D":
                completed_courses.add(course["course_id"])


    remaining_courses = []

    for course_id in required_courses:

        if course_id not in completed_courses:
            remaining_courses.append(course_id)

    grade_points = {
        "A": 4.0, "B": 3.0,
        "C": 2.0, "D": 1.0,
        "F": 0}

    total_points = 0
    course_count = 0

    for course in database.courses.values():

        if student_id in course["grades"]:

            letter_grade = course["grades"][student_id]["grade"]

            total_points += grade_points[letter_grade]

            course_count += 1

    if course_count > 0:
        gpa = total_points / course_count
    else:
        gpa = 0

    current_courses = []

    for course_id, course in database.courses.items():

        if student_id in course["students"]:

            if student_id not in course["grades"]:
                current_courses.append(course_id)

    print("\nAcademic Progress")
    print("--------------------")

    print(f"Major: {major}")
    print(f"GPA: {gpa:.2f}")

    print("\nCompleted Courses:")
    for course in completed_courses:
        print(course)

    print("\nCurrent Courses:")
    for course in current_courses:
        print(course)

    print("\nRemaining Courses:")
    for course in remaining_courses:
        print(course)

#Allows students to view their schedule and see course materials
def view_schedule(student_id):

    enrolled_courses = []

    for section_key, course in database.courses.items():

        if student_id in course["students"]:
            enrolled_courses.append(course)

    if len(enrolled_courses) == 0:
        print("You are not enrolled in any courses.")
        return

    print("\nStudent Schedule")
    print("----------------------")

    for course in enrolled_courses:

        print(f"\nCourse Name: {course['course_name']}")
        print(f"Course ID: {course['course_id']}")
        print(f"Section: {course['section_number']}")
        print(f"Classroom: {course['room']}")
        print(f"Meeting Days: {course['meeting_days']}")
        print(
            f"Time: {course['start_time']} - "
            f"{course['end_time']}"
        )

        print("\nMaterials:")

        if len(course["materials"]) == 0:
            print("   No materials uploaded.")

        else:
            for material in course["materials"]:
                print(
                    f"   {material['title']} "
                    f"({material['file_name']})"
                )

        print("----------------------")


#Main menu for student role options
def student_menu(current_user):

    while True:

        print("\nStudent Menu")
        print("1. Search for Course")
        print("2. Enroll in Course")
        print("3. Academic Progress Tracker")
        print("4. View Schedule")
        print("5. Logout")

        choice = input("Enter 1-5: ")

        match choice:

            case "1":

                course_search()

            case "2":

                course_enroll(current_user["user_id"])

            case "3":

                academic_tracker(current_user["user_id"])

            case "4":

                view_schedule(current_user["user_id"])

            case "5":

                break

            #Checks for user to choose an option between 1 and 5
            case _:

                print("Invalid option.")

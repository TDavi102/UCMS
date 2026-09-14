import database
import authentication

#Provides overall enrollment info for entire school as well
#as enrollment info for each class section
def enrollment_monitor():

    total_enrollment = 0
    total_capacity = 0

    print("\nEnrollment Monitor")
    print("------------------")

    for course_id, course in database.courses.items():

        enrolled = len(course["students"])
        capacity = course["max_seats"]
        available = capacity - enrolled

        total_enrollment += enrolled
        total_capacity += capacity

        print(
            f"{course['course_id']} "
            f"Section: {course['section_number']} | "
            f"{course['course_name']} | "
            f"Enrolled: {enrolled}/{capacity}"
            f"Available seats: {available}")

    print("\nSchool Totals")
    print(
        f"Total Enrollment: "
        f"{total_enrollment}/{total_capacity}"
    )

    if total_capacity > 0:
        percent = (
                total_enrollment /
                total_capacity * 100
        )
    else:
        percent = 0
    print(f"Enrollment Rate: {percent:.1f}%")

#Presents the user with a menu to choose between viewing
#individual student attendance, according to student ID,
#or viewing overall school attendance info
def attendance_monitor():

    while True:

        print("\nAttendance Monitor")
        print("1. School Attendance Report")
        print("2. Search Student Attendance")

        choice = input("Enter 1-2: ")

        if choice == "1":
            break

        elif choice == "2":

            student_id = input(
                "Enter Student ID: "
            )

            found = False

            print("\nStudent Attendance")
            print("------------------")

            for course in database.courses.values():

                if student_id in course["grades"]:

                    attendance = (
                        course["grades"][student_id]
                        ["attendance"]
                    )

                    print(
                        f"{course['course_id']} "
                        f"Section "
                        f"{course['section_number']} | "
                        f"Attendance: "
                        f"{attendance:.1f}%"
                    )

                    found = True

            if not found:
                print(
                    "No attendance records found "
                    "for that student."
                )

            return

        else:
            print(
                "Invalid selection. "
                "Please enter 1 or 2."
            )

    # School-wide attendance report

    school_total_attendance = 0
    school_student_count = 0

    for course in database.courses.values():

        course_total_attendance = 0
        course_student_count = 0

        for student_data in course["grades"].values():

            course_total_attendance += (
                student_data["attendance"]
            )

            course_student_count += 1

        if course_student_count > 0:

            course_average = (
                    course_total_attendance
                    / course_student_count
            )

            print(
                f"{course['course_id']} "
                f"Section "
                f"{course['section_number']} "
                f"| Average Attendance: "
                f"{course_average:.1f}%"
            )

            school_total_attendance += (
                course_total_attendance
            )

            school_student_count += (
                course_student_count
            )

    if school_student_count > 0:

        school_average = (
                school_total_attendance
                / school_student_count
        )

        print(
            f"\nSchool Average "
            f"Attendance: "
            f"{school_average:.1f}%"
        )

    else:
        print("No attendance records found.")

#Calculates gpa for students and presents two menu options:
#1. School Grade Report, 2. Student Grade Report(with a search function
#according to student ID)
def grading_trends_monitor():


    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0}

    while True:

        print("\nGrading Trends Monitor")
        print("1. School Grade Report")
        print("2. Search Student Grades")

        choice = input("Enter 1-2: ")

        if choice == "1":
            break

        elif choice == "2":

            student_id = input("Enter Student ID: ")

            found = False
            total_points = 0
            course_count = 0

            print("\nStudent Grades")
            print("------------------")

            for course in database.courses.values():

                if student_id in course["grades"]:

                    grade = (course["grades"][student_id]["grade"])

                    print(
                        f"{course['course_id']} "
                        f"Section "
                        f"{course['section_number']} | "
                        f"Grade: {grade}")

                    total_points += (grade_points[grade])

                    course_count += 1

                    found = True

            if found:

                gpa = (total_points / course_count)

                print(f"\nStudent GPA: "
                    f"{gpa:.2f}")

            else:

                print(
                    "No grade records found "
                    "for that student.")

            return

        else:

            print("Invalid selection. "
                "Please enter 1 or 2.")

    school_total_points = 0
    school_grade_count = 0

    print("\nCourse GPA Averages")
    print("-------------------")

    for course in database.courses.values():

        course_total_points = 0
        course_grade_count = 0

        for student_data in course["grades"].values():

            grade = student_data["grade"]

            course_total_points += (grade_points[grade])

            course_grade_count += 1

        if course_grade_count > 0:

            course_gpa = (course_total_points / course_grade_count)

            print(
                f"{course['course_id']} "
                f"Section "
                f"{course['section_number']} | "
                f"Average GPA: "
                f"{course_gpa:.2f}"
            )

            school_total_points += course_total_points

            school_grade_count += course_grade_count

        else:

            print(
                f"{course['course_id']} "
                f"Section "
                f"{course['section_number']} | "
                f"No grade data")

    print("\nSchool Totals")

    if school_grade_count > 0:

        school_gpa = (school_total_points /school_grade_count)

        print(f"School Average GPA: "
            f"{school_gpa:.2f}")

    else:

        print("No grading records found.")

#Administrator menu options
def admin_menu(current_user):

    while True:

        print("\nAdministrator Menu")
        print("1. Enrollment Monitor")
        print("2. Attendance Monitor")
        print("3. Grading Trends Monitor")
        print("4. Create New User")
        print("5. Log Out")

        choice = input("Enter 1-5: ")

        match choice:

            case "1":

                enrollment_monitor()

            case "2":

                attendance_monitor()

            case "3":

                grading_trends_monitor()

            case "4":

                authentication.create_user(current_user["role"])

            case "5":

                break

            #Checks if user input is 1-5
            case _:

                print("Invalid option.")








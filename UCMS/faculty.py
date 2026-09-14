
import database

#Checks if classroom is available for the specified
#meeting days and time so the allocator can work
def has_conflict(room, meeting_days,
                 start_time, end_time):

    for scheduled_course in database.classrooms[room]:
        if scheduled_course["meeting_days"] == meeting_days:
            if start_time < scheduled_course["end_time"] and scheduled_course["start_time"] < end_time:
                return True
    return False

#Automates the classroom allocation. Used in create_course function
def allocate_classroom(meeting_days, start_time, end_time):

    for room in database.classrooms:

        if not has_conflict(room, meeting_days,
            start_time, end_time):

            return room

    return None

#Allows faculty to create new courses and automatically
#allocates an open classroom for that course
def create_course(faculty_id):

    course_name = input("Enter course name: ")
    course_id = input("Enter course id: ")
    section_number = input("Enter section number: ")
    meeting_days = input("Enter meeting days: ")
    start_time = int( input("Enter start time (24hr): "))
    end_time = int( input("Enter end time (24hr): "))

    if start_time >= end_time:

        print("End time must be later than start time.")

        return

    max_seats = int( input("Enter max seats: "))

    room = allocate_classroom(meeting_days, start_time, end_time)

    if room is None:

        print("No available classrooms for that time slot")

        return

    section_key = f"{course_id}-{section_number}"

    if section_key in database.courses:
        print("Course section already exists.")
        return

    database.courses[section_key] = {
        "course_id": course_id,
        "course_name": course_name,
        "section_number": section_number,
        "faculty_id": faculty_id,
        "meeting_days": meeting_days,
        "start_time": start_time,
        "end_time": end_time,
        "max_seats": max_seats,
        "room": room,
        "students": [],
        "materials": [],
        "grades": {}
    }

    database.classrooms[room].append({
        "section_key": section_key,
        "course_id": course_id,
        "meeting_days": meeting_days,
        "start_time": start_time,
        "end_time": end_time
    })

    print(f"{course_name} created successfully.")

    print(f"Assigned classroom: {room}")

def upload_materials(faculty_id):

    course_id = input("Enter section key: ")

    if course_id not in database.courses:

        print("Course not found.")

        return

    if database.courses[course_id]["faculty_id"] != faculty_id:

        print("You are not assigned to this course.")

        return

    material_title = input("Enter material name: ")

    file_name = input("Enter file name: ")

    database.courses[course_id]["materials"].append({
        "title": material_title,
        "file_name": file_name
    })

    print("Material uploaded.")

def record_grades(faculty_id):

    section_key = input("Enter section key: ")

    if section_key not in database.courses:

        print("Course not found.")

        return

    if database.courses[section_key]["faculty_id"] != faculty_id:

        print("You are not assigned to this course.")

        return

    students = database.courses[section_key]["students"]

    if len(students) == 0:

        print("No students enrolled.")

        return

    for student_id in students:

        print(f"\nStudent ID: {student_id}")

        while True:

            grade = input("Enter letter grade (A-F): ").upper()

            if grade in ["A", "B", "C", "D", "F"]:
                break

            print("Invalid grade.")

        attendance = float(input("Enter attendance percentage: "))

        if attendance < 0 or attendance > 100:

            print("Attendance must be between 0 and 100.")
        else:

            database.courses[section_key]["grades"][student_id] = {

                "grade": grade,

                "attendance": attendance

            }

    print("Grades recorded successfully.")


def faculty_menu(current_user):

    while True:

        print("\nFaculty Tools Menu")
        print("1. Create Course")
        print("2. Upload Materials")
        print("3. Record Grades")
        print("4. Logout")

        choice = input ("Enter 1-4:")

        match choice:

            case "1":

                create_course(current_user["user_id"])

            case "2":

                upload_materials(current_user["user_id"])

            case "3":

                record_grades(current_user["user_id"])

            case "4":

                break

            case _:

                print("Invalid option.")





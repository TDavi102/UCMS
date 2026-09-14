import authentication
import faculty
import student
import admin

def main():

    #Displays the corresponding menu depending on the user's role
    while True:

        current_user = authentication.login()

        if current_user is None:
            return

        match current_user["role"]:

            case "Student":
                student.student_menu(current_user)

            case "Faculty":
                faculty.faculty_menu(current_user)

            case "Administrator":
                admin.admin_menu(current_user)

if __name__ == "__main__":
    main()
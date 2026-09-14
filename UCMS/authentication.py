import bcrypt
import database

#Function to create new users. Necessary for entire system to run.
#There is an initial ADMIN user hardcoded in the database module
#So that the program can run. ADMIN must create other initial users
def create_user(current_user_role):

    if current_user_role != "Administrator":

        print("Only administrators may create users.")

        return

    while True:

        user_id = input("Enter new user ID: ")

        if user_id not in database.users:
            break

        print("User ID already exists.")

    name = input("Enter name: ")

    while True:

        role = input(
        "Enter role "
        "(Student, Faculty, Administrator): ")

        if role in [
            "Student",
            "Faculty",
            "Administrator"]:

            break

        print("Invalid role.")

    major = None

    if role == "Student":

        while True:
            major = input(
                "Enter major "
                "(Computer Science, Physics): "
            )

            if major in database.degree_requirements:
                break

            print("Invalid major.")

    password = input("Enter password: ")

    #Uses bcrypt to hash entered password for security
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    database.users[user_id] = {

        "name": name,

        "role": role,

        "major": major,

        "password": hashed_password
    }

    print("User created successfully.")

#Asks for log in info so that the rest of the program can run
def login():

    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id not in database.users:

        print("User not found.")
        return None

    stored_hash = database.users[user_id]["password"]

    if bcrypt.checkpw(
            password.encode(),
            stored_hash
    ):

        return {
            "user_id": user_id,
            "role": database.users[user_id]["role"]
        }

    print("Invalid password.")
    return None
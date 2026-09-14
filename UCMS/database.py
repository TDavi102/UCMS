import bcrypt

degree_requirements = {
    "Computer Science": [
        "COP101", "COP102",
        "COP103", "COP104",
        "MAT101", "MAT102",
        "MAT103", "MAT104"
    ],
    "Physics": [
        "PHY101", "PHY102",
        "PHY103", "PHY104",
        "MAT101", "MAT102",
        "MAT103", "MAT104"
    ]
}

users = {

    "ADMIN": {
        "name": "System Administrator",
        "role": "Administrator",
        "major": None,
        "password": bcrypt.hashpw(
            "admin123".encode(),
            bcrypt.gensalt()
        )
    },

    "F001": {
        "name": "John Doe",
        "role": "Faculty",
        "major": None,
        "password": bcrypt.hashpw(
            "faculty123".encode(),
            bcrypt.gensalt()
        )
    },

    "S001": {
        "name": "Jane Doe",
        "role": "Student",
        "major": "Computer Science",
        "password": bcrypt.hashpw(
            "student123".encode(),
            bcrypt.gensalt()
        )
    }
}

courses = {
    "COP101-001": {
        "course_id": "COP101",
        "course_name": "Introduction to Programming",
        "section_number": "001",
        "faculty_id": "F001",
        "meeting_days": "MW",
        "start_time": 900,
        "end_time": 1030,
        "max_seats": 30,
        "room": "A100",
        "students": [],
        "materials": [],
        "grades": {}
    }
}

classrooms = {
    "A100": [
        {
            "section_key": "COP101-001",
            "course_id": "COP101",
            "meeting_days": "MW",
            "start_time": 900,
            "end_time": 1030
        }
    ],

    "A101": [],
    "A102": [],
    "B100": [],
    "B101": [],
    "B102": []
}

#data container for dummy external system integration
attendance_records = {

    "COP101-001": {

        "S001": {
            "total_classes": 15,
            "classes_attended": 14,
            "attendance_percent": 93.3
        },

        "S002": {
            "total_classes": 15,
            "classes_attended": 12,
            "attendance_percent": 80.0
        }
    },

    "MAT101-001": {

        "S001": {
            "total_classes": 12,
            "classes_attended": 11,
            "attendance_percent": 91.7
        }
    }
}
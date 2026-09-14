import database

#Proof of concept third part integration
def get_attendance(section_key, student_id):

    # Future API integration:
    # response = requests.get(
    #     f"https://attendanceapi.edu/attendance/"
    #     f"{section_key}/{student_id}")
    # return response.json()

    return database.attendance_records[section_key][student_id]
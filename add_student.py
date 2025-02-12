from main import app, db, student_information
from datetime import datetime

# Sample Data
student_number = ["22143116", "22143089"]
student_surname = ["Badlon", "Calleja"]
student_firstname = ["Maze Clarion", "Jhay-Em"]
student_middlename = ["Landrito", "Sandrino"]
student_suffix = ["", ""]
student_course = ["BSCS", "BSIT"]
student_year = "3rd Year"
student_section = ["", ""]
student_email = ["badlonmazeclarion@plmun.edu.ph", "callejajhayem_bsit@plmun.edu.ph"]
student_password = ["1234", "1234"]
student_status = "Regular"
student_enrolled = False
student_created = datetime.now()

# Use app.app_context()
with app.app_context():
    # Insert data for all students
    for i in range(len(student_number)):
        record = student_information(
            student_number=student_number[i],
            student_surname=student_surname[i],
            student_firstname=student_firstname[i],
            student_middlename=student_middlename[i],
            student_suffix=student_suffix[i],
            student_course=student_course[i],
            student_year=student_year,
            student_section=student_section[i],
            student_email=student_email[i],
            student_password=student_password[i],
            student_status=student_status,
            student_enrolled=student_enrolled,
            student_created=student_created
        )
        db.session.add(record)

    # Commit to the database
    db.session.commit()
    print("All student data added successfully!")

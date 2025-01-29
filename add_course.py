from main import app, db, college_course_list

# Sample Data
sections = ["3A", "3B", "3C"]
subjects = [
    "Operating Systems",
    "Software Engineering 2 (lec/lab)",
    "Automata Theory And Formal Languages",
    "CS Professional Elective 2",
    "CS Thesis Writing 1",
    "Information Assurance And Security 1",
    "Mathematical Statistics For IT"
]
schedule_time = "07:00AM-09:00AM"
room_section = 201
college_course = "BSCS"
college_year = "3rd Year"
college_day = "M"  # Monday

# Use app.app_context()
with app.app_context():
    # Insert data for all subjects and sections
    for section in sections:
        for subject in subjects:
            record = college_course_list(
                college_course=college_course,
                college_year=college_year,
                college_section=section,
                college_subject=subject,
                college_day=college_day,
                schedule_time=schedule_time,
                room_section=room_section
            )
            db.session.add(record)

    # Commit to the database
    db.session.commit()
    print("All data added successfully!")

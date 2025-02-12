from main import app, db, admin_information
from datetime import datetime

# Sample Data
admin_number = ["11223344", "55667788"]
admin_lastname = ["Chaewon", "Kazuha"]
admin_firstname = ["Kim", "Nakamura"]
admin_middlename = ["Tiger", "Swan"]
admin_suffix = ["", ""]
admin_position = ["Head Admin", "Admin Developer"]
admin_email = ["kimchaewon@plmun.edu.ph", "kazuha@plmun.edu.ph"]
admin_password = ["1234", "1234"]
admin_status = ["Active", "Inactive"]
admin_created = datetime.now()
user_roll = ["Admin", "Admin"]

# Use app.app_context()
with app.app_context():
    # Insert data for all Admins
    for i in range(len(admin_number)):
        record = admin_information(
            admin_number=admin_number[i],
            admin_lastname=admin_lastname[i],
            admin_firstname=admin_firstname[i],
            admin_middlename=admin_middlename[i],
            admin_suffix=admin_suffix[i],
            admin_position=admin_position[i],
            admin_email=admin_email[i],
            admin_password=admin_password[i],
            admin_status=admin_status[i],
            admin_created=admin_created,
            user_roll=user_roll[i] 
        )
        db.session.add(record)

    # Commit to the database
    db.session.commit()
    print("All Admin data added successfully!")

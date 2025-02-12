from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Enum

db = SQLAlchemy()

class college_course_list(db.Model):
    __bind_key__ = 'college_courses'
    id = db.Column(db.Integer, primary_key=True)
    college_course = db.Column(db.String(200), nullable=False)
    college_year = db.Column(db.String(200), nullable=False)
    college_section = db.Column(db.String(200), nullable=False)
    college_subject = db.Column(db.String(200), nullable=False)
    college_day = db.Column(db.String(200), nullable=False)
    schedule_time = db.Column(db.String(200), nullable=False)
    room_section = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<CollegeCourseList %r>' % self.id

class student_information(db.Model):
    __bind_key__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.String(20), nullable=False)
    student_surname = db.Column(db.String(200), nullable=False)
    student_firstname = db.Column(db.String(200), nullable=False)
    student_middlename = db.Column(db.String(200), nullable=False)
    student_suffix = db.Column(db.String(10))
    student_course = db.Column(db.String(100), nullable=False)
    student_year = db.Column(db.String(50), nullable=False)
    student_section = db.Column(db.String(50))
    student_email = db.Column(db.String(200), nullable=False)
    student_password = db.Column(db.String(200), nullable=False)
    student_status = db.Column(db.String(50), nullable=False)
    student_enrolled = db.Column(db.Boolean, nullable=False)
    student_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<StudentInformation %r>' % self.id

class admin_information(db.Model):
    __bind_key__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    admin_number = db.Column(db.String(20), nullable=False)
    admin_position = db.Column(Enum('Database Manager', 'Security', 'Developer', name='user_position'), nullable=False)
    admin_lastname = db.Column(db.String(200), nullable=False)
    admin_firstname = db.Column(db.String(200), nullable=False)
    admin_middlename = db.Column(db.String(200), nullable=False)
    admin_suffix = db.Column(db.String(10))
    admin_email = db.Column(db.String(200), nullable=False)
    admin_password = db.Column(db.String(200), nullable=False)
    admin_status = db.Column(Enum('Active', 'Inactive', 'Missing', name='user_status'), nullable=False)
    user_roll = db.Column(Enum('admin', 'student', 'faculty', name='user_roles'), nullable=False)
    admin_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<AdminInformation %r>' % self.id
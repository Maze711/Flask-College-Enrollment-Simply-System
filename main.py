from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college_course_list.db'
db = SQLAlchemy(app)

class college_course_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college_course = db.Column(db.String(200), nullable=False)
    college_year = db.Column(db.String(200), nullable=False)
    college_section = db.Column(db.String(200), nullable=False)
    college_subject = db.Column(db.String(200), nullable=False)
    college_day = db.Column(db.String(200), nullable=False)
    schedule_time = db.Column(db.String(200), nullable=False)
    room_section = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.id

@app.route('/')
def main():
    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def login():
    student_number = request.form['student_number']
    password = request.form['password']

    if student_number == "student@edu.com" and password == "1234":
        return redirect(url_for('student_information'))
    else:
        return "Invalid Credential or Contact Admin"

@app.route('/student_information')
def student_information():
    return render_template('student_information.html')

@app.route('/view_course')
def view_course():
    course_data = college_course_list.query.all()
    return render_template('view_course.html', courses=course_data)

@app.route('/enroll_course', methods=['GET', 'POST'])
def enroll_course():
    selected_section = None
    if request.method == 'POST':
        selected_section = request.form.get('section')
    if selected_section:
        courses = college_course_list.query.filter_by(college_section=selected_section).all()
    else:
        courses = []

    course_section = college_course_list.query.with_entities(college_course_list.college_section).distinct()
    return render_template('enrollment_page.html', courses=courses, selected_section=selected_section, college_section=course_section)

if __name__ == '__main__':
    app.run(debug=True)
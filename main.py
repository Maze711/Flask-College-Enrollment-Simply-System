from flask import Flask, request, redirect, render_template, url_for
from models import db, college_course_list, student_information

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_BINDS'] = {
    'college_courses': 'sqlite:///college_course_list.db',
    'students': 'sqlite:///student_information.db'
}

db.init_app(app)


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
def student_info_page():
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
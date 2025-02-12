import os
from flask import Flask, request, redirect, render_template, url_for, session
from models import db, college_course_list, student_information

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_BINDS'] = {
    'college_courses': 'sqlite:///college_course_list.db',
    'students': 'sqlite:///student_information.db'
}
app.config['TEMPLATE_DIR'] = 'Student_Portal/'

# Initialize the database
db.init_app(app)

def get_template_path(template_name):
    student_portal_path = os.path.join(app.template_folder, app.config['TEMPLATE_DIR'], template_name)
    main_template_path = os.path.join(app.template_folder, template_name)
    
    if os.path.exists(student_portal_path):
        return f"{app.config['TEMPLATE_DIR']}{template_name}"
    elif os.path.exists(main_template_path):
        return template_name
    else:
        raise FileNotFoundError(f"Template {template_name} not found in either directory.")

@app.route('/')
def main():
    template_path = get_template_path('login_page.html')
    return render_template(template_path)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        student_number = request.form['student_number']
        student_password = request.form['student_password']
        student = student_information.query.filter_by(student_number=student_number, student_password=student_password).first()

        if student:
            if student.student_course == 'BSCS':
                return redirect(url_for('student_info_page', student_number=student.student_number))
            else:
                return "Access restricted to BSCS students only. Please contact the administration for assistance."
        else:
            return "Invalid credentials. Please try again or contact the administrator for assistance."

@app.route('/student_info_page')
def student_info_page():
    student_number = request.args.get('student_number')
    student = student_information.query.filter_by(student_number=student_number).first()
    course_data = college_course_list.query.all()
    template_path = get_template_path('student_info_page.html')
    return render_template(template_path, student=student, courses=course_data)

@app.route('/view_course')
def view_course():
    course_data = college_course_list.query.all()
    template_path = get_template_path('view_course.html')
    return render_template(template_path, courses=course_data)

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
    template_path = get_template_path('enrollment_page.html')
    return render_template(template_path, courses=courses, selected_section=selected_section, college_section=course_section)

@app.route('/logout')
def logout():
    #session.clear()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
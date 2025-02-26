import os
from flask import Flask, request, redirect, render_template, url_for, session
from models import db, college_course_list, student_information, admin_information

try:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_BINDS'] = {
        'college_courses': 'sqlite:///college_course_list.db',
        'students': 'sqlite:///student_information.db',
        'admins': 'sqlite:///admin_information.db'
    }
    app.config['TEMPLATE_DIR'] = 'StudentPortal/'

    # Initialize the database
    db.init_app(app)

    def get_user_role(user_id):
        student = student_information.query.filter_by(student_number=user_id).first()
        admin = admin_information.query.filter_by(admin_id=user_id).first()

        if student:
            return student.user_role
        elif admin:
            return admin.user_role
        else:
            return None

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
            admin = admin_information.query.filter_by(admin_number=student_number, admin_password=student_password).first()
            
            if student and student.student_number == student_number and student.student_password == student_password:
                if student.student_course == 'BSCS':
                    return redirect(url_for('student_info_page', student_number=student.student_number))
                else:
                    return "Access restricted to BSCS students only. Please contact the administration for assistance."
            elif admin and admin.admin_number == student_number and admin.admin_password == student_password:
                return redirect(url_for('view_dashboard'))
            else:
                return "Invalid credentials. Please try again or contact the administrator for assistance."

    @app.route('/student_info_page')
    def student_info_page():
        student_number = request.args.get('student_number')
        student = student_information.query.filter_by(student_number=student_number).first()
        course_data = college_course_list.query.all()
        template_path = get_template_path('StudentPortal/student_info_page.html')
        return render_template(template_path, user_role=student.user_role, student=student, courses=course_data)

    @app.route('/view_course')
    def view_course():
        course_data = college_course_list.query.all()
        template_path = get_template_path('Student_portal/view_course.html')
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
        template_path = get_template_path('Student_portal/enrollment_page.html')
        return render_template(template_path, courses=courses, selected_section=selected_section, college_section=course_section)

    @app.route('/view_dashboard', methods=['GET', 'POST'])
    def view_dashboard():
        selected_course = None  # Stores the selected course
        if request.method == 'POST':
            selected_course = request.form.get('course_list')  # Get selected course from form
        
        # If a course is selected, fetch students for that course; otherwise, return an empty list
        if selected_course:
            students = student_information.query.filter_by(student_course=selected_course).all()
        else:
            students = []  # Empty if no course is selected

        # Fetch distinct course names for dropdown
        college_course = student_information.query.with_entities(student_information.student_course).distinct().all()

        return render_template('AdminPortal/view_dashboard.html', student_list=students, selected_course=selected_course, courses=[c[0] for c in college_course])


    @app.route('/logout')
    def logout():
        #session.clear()
        return redirect(url_for('main'))

except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_information.db'
db = SQLAlchemy(app)

class Student_Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(200), nullable=False)
    student_id = db.Column(db.String(200), nullable=False)
    student_course = db.Column(db.String(200), nullable=False)
    college_year = db.Column(db.String(200), nullable=False)

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
    return render_template('view_course.html')

@app.route('/enroll_course')
def enroll_course():
    return render_template('enrollment_page.html')    

if __name__ == '__main__':
    app.run(debug=True)
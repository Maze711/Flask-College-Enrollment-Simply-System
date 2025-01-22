from flask import Flask, request, redirect, render_template
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

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        student_course = request.form['student_course']
        college_year = request.form['college_year']
        new_student = Student_Information(student_name=student_name, student_id=student_id, student_course=student_course, college_year=college_year)
        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding a student'
    
    else:
        students = Student_Information.query.order_by(Student_Information.student_name).all()
        return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
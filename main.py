from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# class Todo(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(200), nullable=False)
    # description = db.Column(db.String(200), nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
# def main():
#     if request.method == 'POST':
#         task_title = request.form['Title']
#         task_description = request.form['Description']
#         new_task = Todo(title=task_title, description=task_description)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding a task'
    
#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)

def main():
    return("Hello World")

if __name__ == "__main__":
    app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    _tablename_ = 'students'  # Double underscores here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def _repr_(self):  # Double underscores here
        return f'<Student {self.name}>'
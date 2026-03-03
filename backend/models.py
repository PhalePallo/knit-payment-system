from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    bank_account = db.Column(db.String(50))
    students = db.relationship("Student", backref="school", lazy=True)
    payments = db.relationship("Payment", backref="school", lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    payments = db.relationship("Payment", backref="student", lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    knit_fee = db.Column(db.Float, nullable=False)
    school_amount = db.Column(db.Float, nullable=False)
    reference = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
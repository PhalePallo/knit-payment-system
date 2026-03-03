# routes/students.py
from flask import Blueprint, jsonify
from models import Student, Payment

students = Blueprint('students', __name__, url_prefix='/students')

# GET all students
@students.route('/', methods=['GET'])
def get_all_students():
    try:
        all_students = Student.query.all()
        # Always return a list, even if empty
        result = [{"id": s.id, "name": s.name, "school_id": s.school_id} for s in all_students]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Failed to fetch students", "details": str(e)}), 500

# GET payments for a specific student
@students.route('/<int:student_id>/payments', methods=['GET'])
def list_student_payments(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        payments = Payment.query.filter_by(student_id=student_id).all()
        result = [
            {
                "id": p.id,
                "amount": p.amount,
                "knit_fee": p.knit_fee,
                "school_amount": p.school_amount,
                "status": p.status,
                "reference": p.reference,
                "created_at": p.created_at
            }
            for p in payments
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Failed to fetch payments", "details": str(e)}), 500
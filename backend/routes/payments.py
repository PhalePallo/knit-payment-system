# routes/payments.py
from flask import Blueprint, request, jsonify
from models import db, Payment, Student
from sqlalchemy.exc import IntegrityError
import logging

logging.basicConfig(level=logging.INFO)

payments = Blueprint("payments", __name__, url_prefix="/payments")

# ✅ Remove trailing slash to prevent 308 redirect
@payments.route("", methods=["POST"])
def create_payment():
    try:
        data = request.get_json(force=True)
        student_id = data.get("student_id")
        amount = data.get("amount")
        reference = data.get("reference")

        # Validation
        if not student_id:
            return jsonify({"error": "student_id is required"}), 400
        if not reference:
            return jsonify({"error": "reference is required"}), 400
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return jsonify({"error": "amount must be a number"}), 400
        if amount <= 0:
            return jsonify({"error": "amount must be greater than zero"}), 400

        # Check student exists
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"error": f"Student with id {student_id} not found"}), 404

        # Idempotency: reference check
        existing = Payment.query.filter_by(reference=reference).first()
        if existing:
            return jsonify({
                "message": "Payment already exists",
                "payment": {
                    "id": existing.id,
                    "amount": existing.amount,
                    "knit_fee": existing.knit_fee,
                    "school_amount": existing.school_amount,
                    "status": existing.status
                }
            }), 200

        # Calculate fees
        knit_fee = round(amount * 0.02, 2)
        school_amount = round(amount * 0.98, 2)

        # Create payment
        payment = Payment(
            student_id=student.id,
            school_id=student.school_id,
            amount=amount,
            knit_fee=knit_fee,
            school_amount=school_amount,
            reference=reference,
            status="SUCCESS"
        )

        db.session.add(payment)
        db.session.commit()
        logging.info(f"Payment created: {payment}")

        return jsonify({
            "id": payment.id,
            "amount": payment.amount,
            "knit_fee": payment.knit_fee,
            "school_amount": payment.school_amount,
            "status": payment.status
        }), 201

    except IntegrityError as e:
        db.session.rollback()
        logging.error(f"DB error: {str(e)}")
        return jsonify({"error": "Duplicate reference detected"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Something went wrong"}), 500
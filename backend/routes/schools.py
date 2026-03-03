from flask import Blueprint, jsonify
from models import School, Payment

schools = Blueprint('schools', __name__, url_prefix='/schools')

# GET all schools
@schools.route('/', methods=['GET'])
def get_all_schools():
    all_schools = School.query.all()
    result = [{"id": s.id, "name": s.name} for s in all_schools]
    return jsonify(result)

# GET revenue for a specific school
@schools.route('/<int:school_id>/revenue', methods=['GET'])
def get_school_revenue(school_id):
    school = School.query.get(school_id)
    if not school:
        return jsonify({"error": "School not found"}), 404

    payments = Payment.query.filter_by(school_id=school_id).all()
    total_collected = sum(p.amount for p in payments)
    total_knit_fees = sum(p.knit_fee for p in payments)
    total_paid_to_school = sum(p.school_amount for p in payments)

    return jsonify({
        "school": school.name,
        "total_collected": total_collected,
        "total_knit_fees": total_knit_fees,
        "total_paid_to_school": total_paid_to_school
    })
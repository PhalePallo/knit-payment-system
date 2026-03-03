# tests/test_payment.py
import pytest
from app import create_app, db
from models import Student, School

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create test school and student
            school = School(name="Test School", bank_account="12345")
            db.session.add(school)
            db.session.commit()
            student = Student(name="John Doe", school_id=school.id)
            db.session.add(student)
            db.session.commit()
        yield client

def test_create_payment(client):
    response = client.post('/payments', json={
        "student_id": 1,
        "amount": 1000,
        "reference": "INV-TEST-1"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['knit_fee'] == 20.0
    assert data['school_amount'] == 980.0
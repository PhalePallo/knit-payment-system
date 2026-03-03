# seed.py
from app import create_app
from models import db, School, Student

app = create_app()

with app.app_context():
    # Create schools
    school1 = School(name="Greenwood High", bank_account="111111")
    school2 = School(name="Sunrise Academy", bank_account="222222")
    db.session.add_all([school1, school2])
    db.session.commit()

    # Create students
    student1 = Student(name="Alice", school_id=school1.id)
    student2 = Student(name="Bob", school_id=school2.id)
    student3 = Student(name="Charlie", school_id=school1.id)
    db.session.add_all([student1, student2, student3])
    db.session.commit()

    print("✅ Test schools and students added!")
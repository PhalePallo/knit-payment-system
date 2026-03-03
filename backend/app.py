from flask import Flask
from flask_cors import CORS
from models import db, School, Student, Payment
from routes.payments import payments
from routes.schools import schools
from routes.students import students
import os

def create_app():
    app = Flask(__name__)

    # Enable CORS for React
    CORS(app, origins=["http://localhost:3000"])

    # SQLite DB path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "knit_payments.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Register routes
    app.register_blueprint(payments)
    app.register_blueprint(schools)
    app.register_blueprint(students)

    # Create tables
    with app.app_context():
        db.create_all()
        print("✅ Tables created successfully!")

    return app

def seed_data(app):
    with app.app_context():
        if School.query.first():
            print("✅ Data already exists.")
            return

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

        print("✅ Seeded schools and students!")

if __name__ == "__main__":
    app = create_app()
    seed_data(app)
    app.run(debug=True)
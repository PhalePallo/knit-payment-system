# app.py
from flask import Flask
from flask_cors import CORS
from models import db, School, Student, Payment
from routes.payments import payments
from routes.schools import schools
from routes.students import students
import os

def create_app():
    app = Flask(__name__)

    # ✅ Enable CORS for all origins (dev-safe)
    CORS(app, origins="*", supports_credentials=True)

    # Database path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "knit_payments.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(payments)
    app.register_blueprint(schools)
    app.register_blueprint(students)

    # Create tables
    with app.app_context():
        db.create_all()
        print("✅ Tables created!")

    return app

def seed_data(app):
    """Seed schools and students if they don't exist."""
    with app.app_context():
        if School.query.first():
            print("✅ Data already exists, skipping seeding.")
            return

        # Schools
        s1 = School(name="Greenwood High", bank_account="111111")
        s2 = School(name="Sunrise Academy", bank_account="222222")
        db.session.add_all([s1, s2])
        db.session.commit()

        # Students
        st1 = Student(name="Alice", school_id=s1.id)
        st2 = Student(name="Bob", school_id=s2.id)
        st3 = Student(name="Charlie", school_id=s1.id)
        db.session.add_all([st1, st2, st3])
        db.session.commit()

        print("✅ Seeded schools and students!")

if __name__ == "__main__":
    app = create_app()
    seed_data(app)
    app.run(debug=True)
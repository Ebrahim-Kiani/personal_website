from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'  # Table name (optional)flask db migrate -m "Initial migration"
    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Text(), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    DateOfBirth = db.Column(db.DateTime, nullable=True)
    job = db.Column(db.String(50), nullable=True)
    AboutMe = db.Column(db.Text, nullable=True)
    is_admin = db.Column(db.Boolean(), default=False)
    is_active = db.Column(db.Boolean(), default=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    # Add a CheckConstraint to ensure only one row has is_admin=True
    __table_args__ = (
        CheckConstraint('is_admin = (is_admin IS NOT NULL)', name='check_single_admin'),
    )
    def __repr__(self):
        return f"<User {self.id}: {self.fullname}>"

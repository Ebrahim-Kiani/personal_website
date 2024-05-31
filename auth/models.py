from datetime import datetime
from flask_login import UserMixin
from config.settings import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Table name (optional)flask db migrate -m "Initial migration"
    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean(), default=False, unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}: {self.email}>"




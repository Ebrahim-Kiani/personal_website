from datetime import datetime
from flask_login import UserMixin
from config.settings import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Table name (optional)flask db migrate -m "Initial migration"
    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.Text(), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    DateOfBirth = db.Column(db.DateTime, nullable=True)
    job = db.Column(db.String(50), nullable=True)
    AboutMe = db.Column(db.Text, nullable=True)
    is_admin = db.Column(db.Boolean(), default=False, unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def on_model_change(self, form, model, is_created):
        model.updated_on = datetime.now()  # Update the field with the current datetime
        return super().on_model_change(form, model, is_created)
    def __repr__(self):
        return f"<User {self.id}: {self.fullname}>"
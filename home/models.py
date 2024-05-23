from config.settings import db
from auth.models import User


class Resume(db.Model):
    __tablename__ = 'resumes'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    start_year = db.Column(db.Integer(), nullable=False)
    end_year = db.Column(db.Integer(), nullable=False)
    mounth = db.Column(db.Integer(), nullable=True)
    company_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))  # Foreign key reference
    user = db.relationship('User', backref='Resumes')  # Backref to access resumes from User

    def __repr__(self):
        return f"<{self.title}>"


class Skill(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    percent = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))  # Foreign key reference
    user = db.relationship('User', backref='Skills')  # Backref to access resumes from User

    def __repr__(self):
        return f"<{self.title}>"


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))  # Foreign key reference
    user = db.relationship('User', backref='projects')  # Backref to access resumes from User


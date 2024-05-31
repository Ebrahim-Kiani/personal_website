from config.settings import db


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
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))  # Foreign key reference
    user = db.relationship('User', backref='projects')  # Backref to access resumes from User


class Information(db.Model):
    __tablename__ = 'informations'
    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    job = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(250), nullable=True)
    linkedin = db.Column(db.String(150), nullable=True)
    github = db.Column(db.String(150), nullable=True)
    awards = db.Column(db.Integer(), nullable=True)
    Complete_Projects = db.Column(db.Integer(), nullable=True)
    Happy_Customers = db.Column(db.Integer(), nullable=True)
    Cups_of_coffee = db.Column(db.Integer(), nullable=True)
    AboutMe = db.Column(db.Text, nullable=True)
    my_skill = db.Column(db.Text(), nullable=True)
    image1 = db.Column(db.String(255), nullable=True)
    image2 = db.Column(db.String(255), nullable=True)
    resume_file = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))  # Foreign key reference
    user = db.relationship('User', backref='informations')  # Backref to access resumes from User


class ContactMe(db.Model):
    __tablename__ = 'contact me'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    subject = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=True)

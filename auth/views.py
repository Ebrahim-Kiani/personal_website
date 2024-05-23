from getpass import getpass
from password_strength import PasswordPolicy
from flask import request, flash, render_template, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import login_user
from validate_email import validate_email
from auth.models import User, db
from config.settings import app, login
from .admin import admin


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.is_active:
            hashed_password = user.password
            is_valid = bcrypt.check_password_hash(hashed_password, password)
            if is_valid and user.is_admin:
                login_user(user)
                flash('Logged in successfully!', 'success')
                print('logged in')
                return redirect(url_for('admin.index'))

        else:
            print('not login')
            flash('Invalid credentials', 'danger')
    return render_template('login.html')


# Define bcrypt
bcrypt = Bcrypt(app)

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1,
    nonletters=1
)


# Define admin creator
@app.cli.command("create_admin")
def create_admin():
    fullname = input("Enter admin's full name: ")
    email = input("Enter admin's email: ")

    if not validate_email(email):
        print("invalid email(your email must be like email@example.com)")
        return 0

    password = str(getpass("Enter admin's password: "))
    confirm_password = str(getpass("Enter admin's confrim password:"))

    # Test strong of password
    result = policy.test(password)

    if confirm_password != password:
        print("password and confirm passwords do not match")
        return 0

    user_answer = str()
    if len(result) != 0:
        print("Your password is not secure and must meet the minimum requirements below:")
        print(result)
        user_answer = input("Do you want to continue?(Y/n):")

        if user_answer == "n":
            return 0

    elif len(user_answer) == 0 or user_answer == "Y":

        # Generate a hash of the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create the admin user object
        admin_user = User(fullname=fullname, email=email, password=hashed_password, is_admin=True, is_active=True)

        # Add the user object to the database session and commit the changes
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully.")



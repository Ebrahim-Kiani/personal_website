from datetime import datetime
from getpass import getpass
from password_strength import PasswordPolicy
from flask import Flask, request, flash, render_template, redirect, url_for, g
from flask_bcrypt import Bcrypt
from home_module.home import home_bp
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, UserMixin, login_user, logout_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from validate_email import validate_email
from models import User, db

import os

app = Flask(__name__)

# Define data base here

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = b'$2b$12$wqKlYjmOfXPkjfhksfhsk.'  # custom salt

db.init_app(app)  # Initialize SQLAlchemy

# Define modules here
app.register_blueprint(home_bp, url_prefix='')

# Define model(s) Migrate here
migrate = Migrate(app, db)

# Define login here
login = LoginManager(app)
login.login_view = 'login'
@app.before_request
def before_request():
    g.user = current_user

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
      #  remember_me = True if request.form['remember_me'] else False
        user = User.query.filter_by(email=email).first()
        if user and user.is_active:
            hashed_password = user.password
            is_valid = bcrypt.check_password_hash(hashed_password, password)
            if is_valid and user.is_admin:
                login_user(user )
                #g.user = current_user
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


# Set Admin session
class MyModelView(ModelView):
    def is_accessible(self):
        print(current_user.is_authenticated)
        return current_user.is_authenticated and current_user.is_admin


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        print(current_user.is_authenticated)
        return current_user.is_authenticated and current_user.is_admin


# Define admin here
admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Define data base here
#name : value
DATABASE_URL : mysql://flask531_william:sSdif8PXIzY4@services.irn6.chabokan.net:14473/flask531_william
basedir = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///' + os.path.join(basedir, '../mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)  # Initialize SQLAlchemy

# Define security
app.config['SECRET_KEY'] = 'mysecret'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = b'$2b$12$wqKlYjmOfXPkjfhksfhsk.'  # custom salt

app.config['UPLOAD_FOLDER'] = '..\static\images\profile'

from home.views import home_bp
# # Define modules here
app.register_blueprint(home_bp, url_prefix='/')

# Define model(s) Migrate here
migrate = Migrate(app, db)

# Define login here
login = LoginManager(app)
login.login_view = 'login'

from home.models import Skill

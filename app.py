from flask import Flask
from home_module.home import home_bp
from flask_migrate import Migrate
from home_module.models import db
import os

app = Flask(__name__)

# Define data base here

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize SQLAlchemy

# Define modules here
app.register_blueprint(home_bp, url_prefix='')

# Define model(s) Migrate here
migrate = Migrate(app, db)

# Other routes and configurations

if __name__ == '__main__':
    app.run()

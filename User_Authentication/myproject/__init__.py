from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from flask_login import LoginManager


login_manager = LoginManager()
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# configure our application to have management of login users
login_manager.init_app(app)
# tell users which view to go on login
login_manager.login_view = 'login'  # navigate to login view once the user logs in.
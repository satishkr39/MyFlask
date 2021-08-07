from myproject import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin  # UserMixin class has all management features for our users login, logout
from werkzeug.security import generate_password_hash, check_password_hash

# this is to grab particular user and validates it and also show corresponding user page
@login_manager.user_loader
def load_user(user_id):  # this callback is used to reload the user object from the user ID stored in the session.
    return User.query.get(user_id)  # get the rows from db on user_id filters


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(200))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)  # storing password in encrypted format

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash, password)
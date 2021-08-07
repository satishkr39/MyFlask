from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = 'puppies_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    balance = db.Column(db.Integer)

    def __init__(self, name, age, balance=0):
        self.name = name
        self.age    = age
        self.balance = balance

    def __repr__(self):
        return f"Puppy name is {self.name} and {self.age} and {self.balance}"

    def report_toys(self):
        print("Here are my toys")
        for toy in self.toys:  # the toys attribute returns list of toys for Toy Class
            print(toy.item_name)  # item_name attribute of Toy class


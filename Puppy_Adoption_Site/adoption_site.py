# Adoption Site
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate
import os
from forms import AddForm, DelForm

# setting our flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Model class : our tables collection
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The puppy name is {self.name}"

# Views function for HomePage
@app.route('/')
def index():
    return render_template('home.html')

# Home Page for Add Puppy
@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    print(form.name.data)
    print("insdie Add pup method ")
    if form.validate_on_submit():
        print("Inside Add pup Validate ")
        name = form.name.data  # get the data from field
        new_pup = Puppy(name)  # we need to add the name to our model class so creating object.
        db.session.add(new_pup)  # adding to our model table
        print("Puppy Added : ", new_pup)
        db.session.commit()
        return redirect(url_for('list_pupp'))  # if all validated then reidrect to list page
    return render_template('add.html', form=form)  # to render the add page

@app.route('/list')
def list_pupp():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    print(puppies)
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data  # get the data from INT filed
        pupp = Puppy.query.get(id)  # we will get only 1 puppy
        db.session.delete(pupp)
        db.session.commit()
        print("Puppy Deleted: ",pupp)
        return redirect(url_for('list_pupp'))
    return render_template('delete.html', form=form)


if __name__=='__main__':
    app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField(label="Enter name of puppy")
    submit = SubmitField("Add Puppy")


class DelForm(FlaskForm):

    id = IntegerField("Enter the ID to be removed: ")
    submit = SubmitField("Remove Puppy")

class OwnerForm(FlaskForm):
    owner = StringField("Enter Owner Name: ")
    puppy_id = IntegerField("Enter the ID of the puppy: ")
    submit = SubmitField("Submit Owner")
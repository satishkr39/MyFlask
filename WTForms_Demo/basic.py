from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField, SubmitField,
                     SelectField, RadioField)  # Import fields which we want to use
from wtforms.validators import DataRequired  # Importing our required validations

app = Flask(__name__)

# Secret key is required to set up wtforms
app.config['SECRET_KEY'] = 'mysecretkey'  # secret string of our choice


class InfoForm(FlaskForm):  # Creating our class and inheriting FlaskForm
    breed = StringField(label="What breed are you?", validators=[DataRequired()])  # DataRequired() instance is created
    # for validations purpose
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood: ", choices=[('mood_one', 'happy'), ('mood_two', 'Excited')])
    food_choice = SelectField("Please pick your favourite food", choices=[('chi', 'chicken'), ('bf', 'beef'), ('fi', 'fish')])
    feedback = TextAreaField(label="Enter any feedback")
    submit = SubmitField(label="Submit")  # creating submit button parameter


@app.route('/', methods=['GET', 'POST'])
def index():
    # breed = False
    form = InfoForm()  # instance of our class InfoForm
    if form.validate_on_submit():
        # breed = form.breed.data   #get the data from form
        # form.breed.data = ''  # set the data on form
        # session is key value pair of dictionary used to hold values for user login session
        session['breed'] = form.breed.data  # get the breed data from template to py file
        session['neutered'] = form.neutered.data  # get the neutered data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thank_you'))  # this is to redirect user to thank you page when all validation
        # are met upon clicking on submit button.
    return render_template('index.html', form=form)  # this return is to render out initial form and is
    # also our homepage.


@app.route('/thankyou')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)

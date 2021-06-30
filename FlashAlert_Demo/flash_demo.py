from flask import Flask, flash, url_for, redirect, render_template
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# Init our application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'


# define our class and inherit FlaskForm
class FlashFormDemo(FlaskForm):
    submit = SubmitField("Click to Submit")


# define home page
@app.route('/', methods=['GET', 'POST'])
def index():
    my_form = FlashFormDemo()
    if my_form.validate_on_submit():
        flash('You clicked the button')  # this return a iterable object consisting of all messages in
        # get_flashed_messages()
        return redirect(url_for('index'))  # redirecting to same index page
    return render_template('index.html', form=my_form)


if __name__ == '__main__':
    app.run(debug=True)

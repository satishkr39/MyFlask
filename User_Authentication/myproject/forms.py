from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User

# Login Form
class LoginForm(FlaskForm):
    email =StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField("Emai", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    # the password filed and pass_confirm needs to be same in order to pass the EqualTo requirements.
    password = PasswordField("Password: ", validators=[DataRequired(), EqualTo(fieldname='pass_confirm',
                                                                               message="Password must match")])
    pass_confirm = PasswordField("COnfirm Password: ", validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')
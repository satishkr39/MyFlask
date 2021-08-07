from myproject import app, db
from flask import render_template, url_for, flash, abort, redirect, request
from flask_login import login_user, login_required, logout_user

from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out now!!!")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Inside The Login Form")
    form = LoginForm()
    if form.validate_on_submit():
        # Validate whether the user exists or not. Getting the user from db
        user = User.query.filter_by(email=form.email.data).first()
        print("User: ", user)
        print(form.password.data)
        print(user is not None)
        # Here checking the password with Hashed Version if its matching or not.
        if user is not None and user.check_password(password=form.password.data):
            login_user(user)  # if matched then call the in-built login user fn of loginModule which will redirect to home page
            flash("Logged in Success")
            next = request.args.get('next')  # next is inbuild variable in flask login module which hold the last
            # request page by user and once authenticated it will redirect to that page.
            print("NEXT : ",next)
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            return redirect(next)
        flash("Invalid UserName or password")
        print("User Account Not Found")
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print("Inside Register Form")
    form = RegistrationForm()
    # print(form.email.data, form.username.data)
    if form.validate_on_submit():
        print("Register Validated")
        # Check whether the email has been registered or username has been taken
        if form.validate_email(form.email.data):  # passing email to forms class and checking
            print("Email Taken")
            flash("Email has been registered")

        # checking for username existence, if username is taken flash error message
        if form.validate_username(form.username.data):
            print("UserName Taken")
            flash("UserName Has Been Taken")
        user = User(email= form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering")  # this message is passed to html and we can get from get_flashed_messages()
        # then we can iterate over the method to print our flash message on html page.
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def user_base():
    return render_template("username_checker.html")


@app.route('/result')
def username_checker():
    name = request.args.get('username')
    name = str(name)
    lower, upper, digit, special = False, False, False, False
    for i in range(len(name)):
        if name[i].islower(): lower = True
        if name[i].isupper(): upper = True
        if name[i].isdigit(): digit = True
        else:
            special = True
    if lower and upper and digit and special:
        return render_template("username_result.html", name=name, check='Validated')
    else:
        return render_template("username_result.html", name=name, check='Not Validated')


if __name__ == '__main__':
    app.run(debug=True)
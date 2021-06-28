from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index_form():
    return render_template("index_form.html")

@app.route('/signup')
def registration_form():
    return render_template("registration_form.html")

@app.route('/thankyou')
def thank_form():
    first = request.args.get('first')
    last = request.args.get('last')
    print(first, last)
    return render_template('thank_form.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_valid_link.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

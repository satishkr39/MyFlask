from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:500
def index():
    return "<h1>Hello World in Flask!</h1>"


@app.route('/home')  # 127.0.0.1:500/home
def home():
    return "<h1>Hello World in Home!</h1>"


@app.route('/info')  # 127.0.0.1:500/info
def info_page():
    return "<h1> Information Page for my Website! </h1>"


# Dynamic Routing Example
@app.route('/home/<user_name>')
def welcome_user(user_name):
    return "<h2> Hello {}</h2>".format(user_name.upper())


# Debug Mode : This function will fail if we provide string of length less than 20
@app.route('/home/debug/<name>')
def debug_test(name):
    return "The Substring of name is : {}".format(name[20])


if __name__ == '__main__':
    app.run(debug=True)

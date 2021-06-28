from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# Template Inheritance means using a template as common for rest of the webpages. Like common header and footer used in
# all webpages
@app.route('/puppy/<name>')
def home_page(name):
    my_var = name
    return render_template('About_Puppy.html', var_name=my_var)


@app.route('/')
def about_page():
    return render_template('home_puppy.html')


if __name__ == '__main__':
    app.run(debug=True)

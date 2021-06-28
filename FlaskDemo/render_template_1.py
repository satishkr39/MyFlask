from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# Passing the variable from Python to HTML template using {{my_variable}}
@app.route('/')
def home_page():
    my_var = 'Satish'  # Passing a single word
    my_list = ['Apple', 'Bat', 'Cat']  # Passing a list
    my_dict = {1: 'Satish', 2:'Kumar', 3: 'Singh'}  # Passing Dictionary
    return render_template('home.html', var_name=my_var, my_list = my_list, my_dict=my_dict)


@app.route('/about')
def about_page():
    return render_template('about_page.html')


if __name__ == '__main__':
    app.run(debug=True)

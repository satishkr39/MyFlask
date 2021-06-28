from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    print("The passed name is : "+name)
    if str(name).endswith('y'):
        print("Ends with Y")
        name = str(name).replace('y', 'iful')
    else:
        print("Not end with Y")
        name = name + 'y'
    return "<h1> Hello Puppy. Your Latin Name is  {}</h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)
# Function returning function

def hello(name):
    print("Hello Func Called")

    def greet():
        print("Greet Function called")

    def welcome():
        print('Welcome function called')

    if name == 'sk':
        # function is getting returned
        return greet
    else:
        return welcome


x = hello("sk")
print(x())

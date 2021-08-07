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


# DECORATOR DEMO
def new_decorator(func):

    def wrap_func():
        print("Some code before executing func()")

        func()

        print("Some code after executing func()")

        return wrap_func


@new_decorator
def func_need_decorator():
    print("please decorate me")

func_need_decorator()

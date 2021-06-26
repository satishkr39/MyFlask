# INHERITANCE DEMO

class Animal:

    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("Animal Eating")

    def report(self):
        print("Animal Reported")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Created")

    def report(self):
        print("Dog Reported")


myDog = Dog()
print(myDog)

# Access Animal class method from Child(Dog) class
myDog.eat()

# over riding report method of animal class inside the dog class
myDog.report()

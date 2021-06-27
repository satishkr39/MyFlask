class Sample:
    pass


x = Sample()  # creating x of type Sample
print(type(x))


class Dog:
    # def __init__(self, breed):
    #    self.breed = breed

    # CLASS OBJECT ATTRIBUTE IT will always be same for all object of this class
    species = 'Mammal'

    # INIT METHOD CALLED EVERY TIME AN OBJECT IS CREATED
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

# repr returns the string representation of class object. when we print an object this repr is called.
    def __repr__(self):
        return f" Breed: {self.breed}, name: {self.name}"

# it used to return the len() method
    def __len__(self):
        return self.name


# myDog = Dog('Lab')
# print("Breed of myDog is " + myDog.breed)

myDog = Dog('Lab', 'MyDogName')
print(myDog.breed, myDog.name)
print("Printing objects calls repr method: ", myDog)
print(myDog.species)
print(len(myDog))


# CIRCLE CLASS DEMO

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self, radius):
        return self.pi * self.radius * self.radius

    def circumference(self, radius):
        return 2 * self.pi * self.radius


myCircle = Circle()
print("Circle with default value : "+ str(myCircle.area(1)))

myCircle2 = Circle()
print("Circle with radius 10 : "+ str(myCircle2.area(10)))
print("Circumference with radius 10: "+ str(myCircle2.circumference(10)))

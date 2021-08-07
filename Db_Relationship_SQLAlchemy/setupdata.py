# The script to create our puppy, owner, toys and insert in db
from model import db, Puppy, Owner, Toy

'''
# Create 2 puppies
rufus = Puppy('Rufus')
Sammy = Puppy('Sammy')

# Adding puppies to db
db.session.add_all([rufus, Sammy])
db.session.commit()

# Get all puppies
print(Puppy.query.all())
# Grab Rufus from db
rufus = Puppy.query.filter_by(name='Rufus').all()[0]  # gets all the rows having name as rufus and then pick the first item only

# Create owner to Rufus
owner1 = Owner('Owner1', rufus.id)

# Create toys for rufus
toy1 = Toy('Toy_1', rufus.id)
toy2 = Toy('Toy_2', rufus.id)

# commit all changes
db.session.add_all([owner1, toy1, toy2])  # adding all objects at once doesn't cause issue.
db.session.commit()

# get rufus
rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(" ##### RUFUS Details #####", rufus)

# get rufus toys by calling method from Rufus class
rufus.report_toys()'''


# print(Puppy.query.get_or_404(1))
# print all toys of puppy
my_list = Toy.query.filter_by(puppy_id=2).all()
print(my_list)
for item in my_list:
    print(str(item.p)+" and the toys are "+str(item))
print("===========================")
# adding owner to puppy id 2
'''ow1 = Owner('sk', 2)
db.session.add(ow1)
db.session.commit()'''

# print pupyy name of any owner
ow = Owner.query.filter_by(id=2).first()  # direct from owners table
print(" Owner Name ",ow) # op =  Owner Name  the owner name is sk and puppy_id 2 : from Owner class
print("=======================")
# prints the puppy name
ow = Owner.query.filter_by(id=2).first().pw  # using backref we reach to parent table and call the repr fn of that class
print(ow)  # op = Puppy name is Sammy and owner is sk [<Toy 5>, <Toy 6>]: from main Puppy class
print("========================")
# to get the parent class attribute we use backref.attribute
print("puppy name is ",ow.name) # op =  puppy name is  Sammy
print("Puppy Id is ", ow.id) # op = Puppy Id is  2

print(Puppy.query.all())



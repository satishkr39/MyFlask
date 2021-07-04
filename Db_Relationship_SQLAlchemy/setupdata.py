# The script to create our puppy, owner, toys and insert in db
from model import db, Puppy, Owner, Toy

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
rufus.report_toys()



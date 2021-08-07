# The script to create our puppy, owner, toys and insert in db
from CRUD_SQLAlchemy import db, Puppy

# Create 2 puppies

#rufus = Puppy('Rufus', 21, 100)
#Sammy = Puppy('Sammy' ,22, 200)
#Tom = Puppy('Tommy' ,23, 300) */

# Adding puppies to db
#db.session.add_all([rufus, Sammy, Tom])
#db.session.commit()

# Get all puppies
print(Puppy.query.all()[0].name)
puppy_1 = Puppy.query.all()[0]
print(puppy_1.name)
# Grab Rufus from db
rufus = Puppy.query.filter_by(name='Rufus').all()[0]  # gets all the rows having name as rufus and then pick the first item only



# get rufus
rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(" ##### RUFUS Details #####", rufus)



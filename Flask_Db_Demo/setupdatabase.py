from basic import db, Puppy
# Create the tables in the database
db.create_all()

# Create new entries in the database
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)
# Check ids (haven't added sam and frank to database, so they should be None)
print(sam.id)
print(frank.id)
db.session.add_all([sam, frank])  # adding multiple rows at once
db.session.commit()  # committing changes to DB
# Check the ids it won't be null as it got inserted in db

# CREATE
my_puppy = Puppy('Rufus', 1)  # Creating puppy object using our model class puppy
db.session.add(my_puppy)  # adding our puppy to session
db.session.commit()  # pushing puppy to db

# READ, Read all puppies
all_puppies = Puppy.query.all()
print(all_puppies)

# Read by ID
# puppy_one = Puppy.query.get(1)
# print(puppy_one.name)

# FILTER BY NAME OR ID
puppy_filter = Puppy.query.filter_by(name='Rufus')  # get the rows having name='Rufus'
print(puppy_filter.all())

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# DELETE
second_puppy = Puppy.query.get(1)
print(second_puppy)
db.session.delete(second_puppy)
db.session.commit()

# Read all puppies
all_puppies = Puppy.query.all()
print(all_puppies)




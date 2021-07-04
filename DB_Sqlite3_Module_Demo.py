import sqlite3

conn = sqlite3.connect("my_test.sqlite")
print(sqlite3.version_info)
print(sqlite3.version)

curr = conn.cursor()

curr.execute('''DROP TABLE IF Exists Counts''') # DROP TABLE IF EXISTS
curr.execute('''CREATE TABLE Counts (name TEXT, Roll INTEGER)''')  # Create Table
# Insert values
curr.execute('''INSERT INTO Counts VALUES('Satish', 1)''')
curr.execute('''INSERT INTO Counts VALUES('Kumar', 2)''')
curr.execute('''INSERT INTO Counts VALUES('Singh', 3)''')
conn.commit()

# User Input insertion to db
name = input("Enter Name")
roll = input("Input Roll Number")
curr.execute('''INSERT INTO Counts VALUES(?, ?)''',(name, roll))
conn.commit()

# The qmark style used with executemany(): to insert more rows at once
insert_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
curr.executemany("insert into Counts values (?, ?)", insert_list)
conn.commit()

# Printing all rows from table Counts
for row in curr.execute('''SELECT * FROM Counts'''):
    print(row)
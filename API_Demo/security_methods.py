# this would be a database table

from Model import User

users = [User(1,'Jose','mypassword'), User(2,'Mimi','secret')]  # 2 instance of User class

username_table = {u.username:u for u in users}  # creating dict having username and entire property as value
print(username_table)

userid_table = {u.id : u for u in users}  # dict having ID as key and other properties as value.
print(userid_table)

# Authenticate Method : Checks user exists or not and return user if found
def authenticate(username, password):
    user = username_table.get(username, None)  # Returns None if username is not found
    if user and password == user.password:
        return user

def identity(payload):  # payload is the content of the JWT.
    user_id = payload['identity']  # gets the payload identity value
    return userid_table.get(user_id, None)  # then uses the user_id to get from user_table if exits else return None
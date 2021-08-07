class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"The name is {self.username} and password is {self.password}"

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
print(type(username_table))
print(username_table.get('u2', None))
print(username_table)
for u in users:
    print(u.username)
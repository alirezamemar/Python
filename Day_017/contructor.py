class User:
    def __init__(self, user_id, username): # user_id is a parameter and id is an attribute
        self.id = user_id
        self.username = username
        self.follower = 0

user_1 = User(1, "Test")
print(user_1.id, user_1.username, user_1.follower)

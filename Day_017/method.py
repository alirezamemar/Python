class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.uername = username
        self.followers = 0
        self.following = 0

    def follower(self, user):
        user.followers +=1 
        self.following +=1 

user_1 = User(1, "user1")
user_2 = User(2, "user2")
user_1.follower(user_2)

print(user_1.followers, user_2.followers, user_1.following, user_2.following)
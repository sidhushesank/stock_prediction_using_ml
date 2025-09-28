from flask_login import UserMixin

# Hardcoded users dictionary: username -> (id, password)
USERS = {
    "user1": {"id": 1, "password": "password1"},
    "user2": {"id": 2, "password": "password2"}
}

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get(user_id):
        for username, u in USERS.items():
            if u['id'] == int(user_id):
                return User(u['id'], username)
        return None

    @staticmethod
    def validate(username, password):
        user = USERS.get(username)
        if user and user['password'] == password:
            return User(user['id'], username)
        return None

users = []

def get_users():
    return users

def add_user(user):
    users.append(user)
    return user

def get_user_by_username(username):
    for user in users:
        if user.username == username:
            return user
    return None

def delete_user_by_username(username):
    for user in users:
        if user.username == username:
            users.remove(user)
            return user
    return None

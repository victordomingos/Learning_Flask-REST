from user import User
from werkzeug.security import safe_str_cmp


# Table users (pseudo DB)
users = {
    User(1, 'Bob', 'asdf'),
    User(2, 'victor', '1234'),
}


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)  # By default, returns None in case no username provided
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        print("returning user")
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

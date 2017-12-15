from user import User
from werkzeug.security import safe_str_cmp


# Table users (pseudo DB)
users = {
    User(1, 'Bob', 'asdf'),
    User(2, 'victor', '1234'),
}


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

"""
username_mapping = { 'Bob': {
    'id': 1
    'username': 'Bob'
    'password': 'asdf'
    }
}



userid_mapping = { 1: {
    'id': 1
    'username': 'Bob'
    'password': 'asdf'
    }
}
"""


def authenticate(username, password):
    user = username_mapping.get(username, None)  # By default, returns None in case no username provided
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

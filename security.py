from user import User

# Table users (pseudo DB)
users = {
    User(1, 'Bob', 'asdf')
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
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)
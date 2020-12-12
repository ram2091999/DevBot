import os
import pickle
from functools import wraps


def check_auth_state(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, 'user_state/user.p')
        file_name = os.path.abspath(os.path.realpath(file_path))
        user = None
        try:
            user = pickle.load(open(file_name, 'rb'))
            is_authenticated = True
        except Exception:
            is_authenticated = False
        
        func(*args, is_authenticated=is_authenticated, user=user, **kwargs)
    return wrapper_func

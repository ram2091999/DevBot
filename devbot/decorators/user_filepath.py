import os
from functools import wraps


def get_user_filepath(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, 'user_state/user.p')
        file_name = os.path.abspath(os.path.realpath(file_path))
        func(*args, user_file_path=file_name, **kwargs)
    return wrapper_func

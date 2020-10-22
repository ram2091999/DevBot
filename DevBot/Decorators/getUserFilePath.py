import os,pickle
from functools import wraps


def getUserFilePath(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        file_path =  os.path.join( fileDir, 'userState/user.p')
        filename = os.path.abspath(os.path.realpath(file_path))
        func(*args,userFilePath = filename,**kwargs) 
    return wrapper_func
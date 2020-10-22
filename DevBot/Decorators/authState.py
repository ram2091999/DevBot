import os,pickle
from functools import wraps


def checkAuthState(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        file_path =  os.path.join( fileDir, 'userState/user.p')
        filename = os.path.abspath(os.path.realpath(file_path))
        user = None
        try:
            user = pickle.load(open(filename,'rb'))
            checkAuthState = True
        except:
            checkAuthState = False
        
        func(*args,authState=checkAuthState,user=user,**kwargs) 
    return wrapper_func
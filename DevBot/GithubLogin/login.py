import click
from github import Github
import requests
import logging
import os
import pickle




@click.command()
@click.option('--username', prompt="Your Github Username")
@click.option('--password', prompt=True,hide_input=True)
def login(username, password):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    file_path =  os.path.join( fileDir, 'userState/user.p')
    filename = os.path.abspath(os.path.realpath(file_path))
    try:
        user = pickle.load(open(filename,'rb'))
        checkAuthState = True
    except:
        checkAuthState = False


    if checkAuthState:
        print(f"\033[93mYou've already logged in as {user.get_user().login}. Run `devbot logout` to Log out\033[0m")
        
        
        return
    r = requests.get('https://api.github.com', auth=(username, password))
    if r.status_code < 400:
        
        user = Github(username,password)
        print(f"\033[92mLogged in Successfully\033[0m")
        
        pickle.dump( user, open( filename, "wb" ) )
    else:
        print(f"\033[91mCould not log in\033[0m")
    
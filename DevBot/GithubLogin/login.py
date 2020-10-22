import click
from github import Github
import requests
import os
import pickle
from ..Decorators.authState import checkAuthState 
from ..Decorators.getUserFilePath import getUserFilePath


@click.command()
@click.option('--username', prompt="Your Github Username")
@click.option('--password', prompt=True,hide_input=True)
@getUserFilePath
@checkAuthState
def login(username, password,authState,user,userFilePath):
    checkAuthState = authState
    if checkAuthState:
        print(f"\033[93mYou've already logged in as {user.get_user().login}. Run `devbot logout` to Log out\033[0m")
        return
    r = requests.get('https://api.github.com', auth=(username, password))
    if r.status_code < 400: 
        user = Github(username,password)
        print(f"\033[92mLogged in Successfully\033[0m")
        
        pickle.dump( user, open( userFilePath, "wb" ) )
    else:
        print(f"\033[91mCould not log in\033[0m")
    
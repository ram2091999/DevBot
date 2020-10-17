import click
from github import Github
import requests
import logging
import os
import pickle




@click.command()
def logout():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    file_path =  os.path.join( fileDir, 'userState/user.p')
    filename = os.path.abspath(os.path.realpath(file_path))
    try:
        os.remove(filename)
        print(f"\033[92mLogged out Successfully\033[0m")
    except:
        print(f"\033[91mYou're not logged in. run `devbot login` to login\033[0m")

    
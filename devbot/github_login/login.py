import click
from github import Github
import requests
import pickle
from ..decorators.auth_state import check_auth_state
from ..decorators.user_filepath import get_user_filepath


@click.command()
@click.option('--username', prompt="Your Github Username")
@click.option('--password', prompt=True, hide_input=True)
@get_user_filepath
@check_auth_state
def login(username, password, is_authenticated, user, user_file_path):
    if is_authenticated:
        print(f"\033[93mYou've already logged in as {user.get_user().login}. Run `devbot logout` to Log out\033[0m")
        return
    res = requests.get('https://api.github.com', auth=(username, password))
    if res.status_code < 400:
        user = Github(username, password)
        print(f"\033[92mLogged in Successfully\033[0m")
        pickle.dump(user, open(user_file_path, "wb"))
    else:
        print(f"\033[91mCould not log in\033[0m")

import click
import os
from ..decorators.auth_state import check_auth_state
from ..decorators.user_filepath import get_user_filepath


@click.command()
@get_user_filepath
@check_auth_state
def logout(is_authenticated, user, user_file_path):
    if is_authenticated:
        os.remove(user_file_path)
        print(f"\033[92mLogged out Successfully\033[0m")
    else:
        print(f"\033[91mYou're not logged in. run `devbot login` to login\033[0m")

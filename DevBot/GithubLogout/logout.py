import click
import os
from ..Decorators.authState import checkAuthState 
from ..Decorators.getUserFilePath import getUserFilePath



@click.command()
@getUserFilePath
@checkAuthState
def logout(authState,user,userFilePath):
    if authState:
        os.remove(userFilePath)
        print(f"\033[92mLogged out Successfully\033[0m")
    else:
        print(f"\033[91mYou're not logged in. run `devbot login` to login\033[0m")

        

    
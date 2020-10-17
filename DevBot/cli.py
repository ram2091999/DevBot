import click
from .GithubLogin import login as login_command
from .GithubLogout import logout as logout_command


@click.group()
def cli():
    pass

cli.add_command(login_command.login)
cli.add_command(logout_command.logout)


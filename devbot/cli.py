import click
from .github_login import login as login_command
from .github_logout import logout as logout_command
from .config import config as config_commands


@click.group()
def cli():
    pass


cli.add_command(login_command.login)
cli.add_command(logout_command.logout)
cli.add_command(config_commands.config)

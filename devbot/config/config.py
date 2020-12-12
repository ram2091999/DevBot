import click
import os
import pickle


def get_configs():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'user_state/config.p')
    file_name = os.path.abspath(os.path.realpath(file_path))
    configs = None
    config_is_present = False

    try:
        configs = pickle.load(open(file_name, 'rb'))
        config_is_present = True
    except Exception:
        pass

    if not config_is_present:
        return "~/Desktop/git-workspace"
    else:
        return configs["workDirectory"]


@click.command()
@click.option('--work-directory', prompt="Work Directory",
              default=lambda: get_configs(), show_default=True)
def config(work_directory):
    configs = {"workDirectory": work_directory}
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'user_state/config.p')
    file_name = os.path.abspath(os.path.realpath(file_path))
    pickle.dump(configs, open(file_name, "wb"))
    print(f"\033[92mSuccessfully updated config\033[0m")

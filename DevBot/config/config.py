import click
from github import Github
import requests
import os
import pickle


def getConfigState():    
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    file_path =  os.path.join( fileDir, 'userState/config.p')
    filename = os.path.abspath(os.path.realpath(file_path))
    config = None
    isConfigPresent = False
    try:
        config = pickle.load(open(filename,'rb'))
        isConfigPresent = True
    except:
        pass

    if not isConfigPresent:
        return "~/Desktop/git-workspace"
    else:
        return config["defaultWorkDirectory"]

            
    



@click.command()
@click.option('--defaultworkDirectory', prompt="Your Default Work Directory",default=lambda : getConfigState(),show_default=True)
def config(defaultworkdirectory):
    config = {}
    config["defaultWorkDirectory"] = defaultworkdirectory
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    file_path =  os.path.join( fileDir, 'userState/config.p')
    filename = os.path.abspath(os.path.realpath(file_path))
    pickle.dump( config , open( filename , "wb" ) )
    print(f"\033[92mSuccessfully updated config\033[0m")




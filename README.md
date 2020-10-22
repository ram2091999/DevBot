# DevBot
Devbot is a CLI to make development faster. It lets you manage multiple projects by having a separate to-do list for each one and it is also integrated with github which allows you to push the to-do list that you created to GitHub.

### Currently available commands

1. `devbot login` : This command allows you to login to github. It then stores the session as a pickle file locally.

2. `devbot logout` : This command logs out if you've already logged in.


### How I wish to expand 

The CLI should have a list of projects the user is working on currently and each one has it's own to-do list. If the user is mentioned in any issue or PR, this should automatically update the list. Also, if the user wishes, he should be able to push the to-do list to the Project section of GitHub. Also, for each project, the user should be able to write custom pre-push test commands.


### Requirements 
 
1. Python (version 3.6 or above)

### How to set-up

1. `git clone https://github.com/ram2091999/DevBot.git`

2. `pip3 install virtualenv`

3. cd into the directory

4. `virtualenv venv`

5. `source venv/bin/activate`

6. `pip3 install --editable .`

7. `devbot --help`







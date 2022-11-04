import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users )
from App.controllers import ( create_group, get_all_groups_json, get_all_groups )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 
group_cli = AppGroup('group', help='Group object commands')

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())


#group
# Then define the command and any parameters and annotate it with the group (@)
@group_cli.command("create", help="Creates a group")
@click.argument("groupname", default="Customer Group")
@click.argument("password", default="Customer Grouppass")
def create_group_command(username, password):
    create_group(groupname, password)
    print(f'{groupname} created!')

# this command will be : flask group create Customer Group Customer Grouppass

@group_cli.command("list", help="Lists groups in the database")
@click.argument("format", default="string")
def list_group_command(format):
    if format == 'string':
        print(get_all_groups())
    else:
        print(get_all_groups_json())

app.cli.add_command(user_cli) # add the group to the cli
app.cli.add_command(group_cli) # add the group to the cli


'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
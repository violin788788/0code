import os


"""
commands = [
    "git add -A",
    'git commit -m "update/create/delete files+folders"'
]

"""

commands = [

			"git status"

]

# Execute the commands in the shell using os.system()
for command in commands:
    os.system(command)

import subprocess
import os
repos=["info34","vote34","trading",""]
commands=["git status"]
for repo in repos:
    if not os.path.isdir(repo):
        continue
    print("--- Running in",repo,"---")
    for command in commands:
        subprocess.run(command,shell=True,cwd=repo)

import subprocess
import os
cwd=os.getcwd()
repos=["info34","vote34","info34\\trading",""]
commands=["git status"]
for repo in repos:
    print("--------------------------------------------")
    check=os.path.join(cwd,repo)
    print("--- Running in",check,"---")
    for command in commands:
        subprocess.run(command,shell=True,cwd=check)

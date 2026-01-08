
import subprocess
folder=r"A:\Users\-\0code\dist\screenshot"
script="copy_files.py"
icon="screenshot.ico"
cmd=f'pyinstaller --onefile --add-data "{folder};screenshot" --icon="{icon}" {script}'
subprocess.run(cmd,shell=True)



"""import os,subprocess,sys
#folder="dist\\screenshot"
folder="screenshot"
script="copy_files.py"
cmd=f'pyinstaller --onefile --add-data "{folder};{folder}" {script}'
subprocess.run(cmd,shell=True)

"""
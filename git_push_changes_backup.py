import subprocess,os
repo_path=r"A:\Users\-\0code"
github_user="violin788788"
repo_name="0code"
token_file=r"A:\Users\-\0code\git_token\git_token.txt"
with open(token_file,"r") as f: token=f.read().strip()
os.chdir(repo_path)
subprocess.run(["git","init"],shell=True)
subprocess.run(["git","remote","remove","origin"],shell=True)
subprocess.run(["git","branch","-M","main"],shell=True)
changed_files=subprocess.check_output(["git","status","--porcelain"],text=True).splitlines()
files_to_add=[]
for line in changed_files:
    file_name=line.split()[-1]
    if "." in file_name and os.path.isfile(file_name):
        files_to_add.append(file_name)
for f in files_to_add:
    print("Adding:",f)
    subprocess.run(["git","add",f],shell=True)
if files_to_add:
    subprocess.run(["git","commit","-m","Update files with dots"],shell=True)
    repo_url=f"https://{token}@github.com/{github_user}/{repo_name}.git"
    subprocess.run(["git","remote","add","origin",repo_url],shell=True)
    print("Pushing to GitHub...")
    subprocess.run(["git","push","-u","--force","origin","main"],shell=True)
    print("Push complete!")
else:
    print("No changed files with a '.' to push.")

import subprocess,os

repo_path=r"A:\Users\-\0code"
github_user="violin788788"
repo_name="0code"
token_file=r"A:\Users\-\0code\git_token\git_token.txt"

with open(token_file,"r") as f: token=f.read().strip()
os.chdir(repo_path)
subprocess.run(["git","init"],shell=True)
subprocess.run(["git","config","user.name","LocalUser"],shell=True)
subprocess.run(["git","config","user.email","local@example.com"],shell=True)
subprocess.run(["git","branch","-M","main"],shell=True)
subprocess.run(["git","rm","-r","--cached","."],shell=True)  # remove all tracked files

files_to_add=[f for f in os.listdir(repo_path) if os.path.isfile(f) and "." in f]
for f in files_to_add: print("Adding:",f); subprocess.run(["git","add",f],shell=True)
subprocess.run(["git","commit","-m","Sync PC files with GitHub"],shell=True)

repo_url=f"https://{token}@github.com/{github_user}/{repo_name}.git"
subprocess.run(["git","remote","remove","origin"],shell=True)
subprocess.run(["git","remote","add","origin",repo_url],shell=True)
print("Pushing to GitHub..."); subprocess.run(["git","push","-u","--force","origin","main"],shell=True)
print("Push complete!")

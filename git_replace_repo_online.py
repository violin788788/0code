import subprocess,os
repo_path=r"A:\Users\-\0code"
github_user="violin788788"
repo_name="0code"
token_file=r"A:\Users\-\0code\git_token\git_token.txt"
with open(token_file,"r") as f: token=f.read().strip()
os.chdir(repo_path)
subprocess.run(["git","remote","remove","origin"],shell=True)
subprocess.run(["git","init"],shell=True)
files_to_add=[f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path,f))]
if not files_to_add: print("No files to push."); exit()
for f in files_to_add: print("Adding:",f); subprocess.run(["git","add",f],shell=True)
subprocess.run(["git","commit","-m","Push only files, skip directories"],shell=True)
subprocess.run(["git","branch","-M","main"],shell=True)
repo_url=f"https://{token}@github.com/{github_user}/{repo_name}.git"
subprocess.run(["git","remote","add","origin",repo_url],shell=True)
print("Pushing to GitHub..."); subprocess.run(["git","push","-u","--force","origin","main"],shell=True)
print("Push complete!")

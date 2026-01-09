from github import Github
import os,hashlib
script_dir=os.path.dirname(os.path.abspath(__file__))
token_file=os.path.join(script_dir,"token.txt")
local_base="/home/info34/mysite"
remote_base="mysite"
github_user="violin788788"
repo_name="info34"
with open(token_file,"r") as f: token=f.read().strip()
g=Github(token)
repo=g.get_user().get_repo(repo_name)
def get_all_remote_files(path=remote_base):
    files={}
    try: contents=repo.get_contents(path)
    except: return files
    for item in contents:
        if item.type=="file": files[item.path]=item
        else: files.update(get_all_remote_files(item.path))
    return files
def get_all_local_files():
    out=[]
    for root,_,files in os.walk(local_base):
        for f in files:
            full=os.path.join(root,f)
            rel=os.path.relpath(full,local_base)
            out.append((full,f"{remote_base}/{rel}".replace("\\","/")))
    return out
remote_files=get_all_remote_files()
local_files=get_all_local_files()
num_files=len(local_files)
count=0
for local_path,remote_path in local_files:
    count+=1
    print(f"{count} {num_files}",end="\r")
    with open(local_path,"r",encoding="utf-8",errors="ignore") as file: content=file.read()
    local_hash=hashlib.sha1(content.encode()).hexdigest()
    commit_msg=f"Sync {remote_path}"
    if remote_path in remote_files:
        remote_hash=hashlib.sha1(remote_files[remote_path].decoded_content).hexdigest()
        if local_hash!=remote_hash:
            repo.update_file(remote_path,commit_msg,content,remote_files[remote_path].sha)
            print(f"Updated {remote_path}")
        else: print(f"Skipped {remote_path}")
        del remote_files[remote_path]
    else:
        repo.create_file(remote_path,commit_msg,content)
        print(f"Created {remote_path}")
count=0
for f,file_obj in remote_files.items():
    count+=1
    print(f"{count} {num_files}",end="\r")
    try:
        repo.delete_file(f,f"Remove {f}",file_obj.sha)
        print(f"Deleted {f}")
    except: continue

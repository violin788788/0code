from github import Github
import os, hashlib
repo_path = os.getcwd()
token_file = repo_path+r"\token-git\token-git.txt"
github_user = "violin788788"
repo_name = os.path.basename(repo_path)
with open(token_file,"r") as f: token = f.read().strip()
g = Github(token)
repo = g.get_user().get_repo(repo_name)
def get_all_remote_files(path=""):
    files = {}
    contents = repo.get_contents(path)
    for item in contents:
        if item.type == "file":
            files[item.path] = item
        elif item.type == "dir":
            files.update(get_all_remote_files(item.path))
    return files
def local_files_in_root():
    return [f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path,f)) and "." in f]
remote_files = get_all_remote_files()
local_files = local_files_in_root()
num_files = len(local_files)
count=0
for f in local_files:
    count=count+1
    #print(count,num_files)
    print(f"{count} {num_files}", end="\r")
    full_path = os.path.join(repo_path,f)
    with open(full_path,"r",encoding="utf-8",errors="ignore") as file: content = file.read()
    local_hash = hashlib.sha1(content.encode()).hexdigest()
    commit_msg = f"Sync {f}"
    if f in remote_files:
        remote_hash = hashlib.sha1(remote_files[f].decoded_content).hexdigest()
        if local_hash != remote_hash:
            repo.update_file(f, commit_msg, content, remote_files[f].sha)
            print(f"Updated {f}")
        else:
            print(f"Skipped {f} (unchanged)")
        del remote_files[f]
    else:
        repo.create_file(f, commit_msg, content)
        print(f"Created {f}")
count=0          
# Delete remaining remote files (these do not exist locally)
for f, file_obj in remote_files.items():
    count=count+1
    print(f"{count} {num_files}", end="\r")
    try: 
        repo.delete_file(f, f"Remove {f}", file_obj.sha)
        print(f"Deleted {f}")
    except:
        continue
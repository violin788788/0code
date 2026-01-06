from github import Github
import os, hashlib

repo_path = r"A:\Users\-\0code"
token_file = r"A:\Users\-\0code\git_token\git_token.txt"
github_user = "violin788788"
repo_name = "0code"

with open(token_file,"r") as f: token = f.read().strip()
g = Github(token)
repo = g.get_user().get_repo(repo_name)

local_files = [f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path,f)) and "." in f]
remote_files = {f.path: f for f in repo.get_contents("")}

# Update or create files
for f in local_files:
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
        del remote_files[f]  # Mark as processed
    else:
        repo.create_file(f, commit_msg, content)
        print(f"Created {f}")

# Delete files on GitHub that are not in local folder
for f, file_obj in remote_files.items():
    repo.delete_file(f, f"Remove {f}", file_obj.sha)
    print(f"Deleted {f}")

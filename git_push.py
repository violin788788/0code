from github import Github
import os, hashlib

repo_path = r"A:\Users\-\0code"
token_file = r"A:\Users\-\0code\git_token\git_token.txt"
github_user = "violin788788"
repo_name = "0code"

with open(token_file,"r") as f: token = f.read().strip()
g = Github(token)
repo = g.get_user().get_repo(repo_name)

# Get local files to be pushed (only files with a "." in the root folder)
local_files = [f for f in os.listdir(repo_path) if os.path.isfile(os.path.join(repo_path,f)) and "." in f]

# Get remote files from the GitHub repo (root level only)
remote_files = {f.path: f for f in repo.get_contents("")}

# Update or create files on GitHub
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
        del remote_files[f]  # Mark this file as processed
    else:
        repo.create_file(f, commit_msg, content)
        print(f"Created {f}")

# Delete files on GitHub that do not exist locally (and ensure it's not a directory)
for f, file_obj in remote_files.items():
    if file_obj.type == "file":  # Only delete files, not directories
        repo.delete_file(f, f"Remove {f}", file_obj.sha)
        print(f"Deleted {f}")
    else:
        print(f"Skipped {f} (directory, not a file)")

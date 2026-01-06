from github import Github
import os

repo_path = r"A:\Users\-\0code"
token_file = r"A:\Users\-\0code\git_token\git_token.txt"
github_user = "violin788788"
repo_name = "0code"

with open(token_file,"r") as f: token = f.read().strip()
g = Github(token)
repo = g.get_user().get_repo(repo_name)

for f in os.listdir(repo_path):
    full_path = os.path.join(repo_path,f)
    if os.path.isfile(full_path) and "." in f:
        with open(full_path,"r",encoding="utf-8",errors="ignore") as file: content = file.read()
        commit_msg = f"Update {f}"
        try:
            contents = repo.get_contents(f)
            remote_content = contents.decoded_content.decode()
            if content != remote_content:
                repo.update_file(contents.path, commit_msg, content, contents.sha)
                print(f"Updated {f}")
            else:
                print(f"Skipped {f} (no changes)")
        except:
            repo.create_file(f, commit_msg, content)
            print(f"Created {f}")

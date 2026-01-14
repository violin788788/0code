from github import Github


from github import Github
import os

REPO = "violin788788/0code"
BRANCH = "main"
OUT_DIR = "repo_pulled"

g = Github()
repo = g.get_repo(REPO)

def pull_contents(path=""):
    contents = repo.get_contents(path, ref=BRANCH)
    for item in contents:
        if item.type == "dir":
            pull_contents(item.path)
        else:
            local_path = os.path.join(OUT_DIR, item.path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, "wb") as f:
                f.write(item.decoded_content)

pull_contents()
print("All files pulled successfully!")



"""
# Repo and branch
REPO = "violin788788/0code"
BRANCH = "main"
#FILE = "/home/info66/mysite/templates/info"
FILE = "info_pulled"

# Connect to GitHub (no token needed for public repos)
g = Github()
repo = g.get_repo(REPO)

# Pull latest info.html
try:
    file_content = repo.get_contents("info.html", ref=BRANCH)
    with open(FILE+"_new"+".html", "w") as f:
        f.write(file_content.decoded_content.decode())
    print("info.html pulled successfully!")
except Exception as e:
    print("Failed to pull info.html:", e)
"""
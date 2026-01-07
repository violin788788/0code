from github import Github

# Repo and branch
REPO = "violin788788/info"
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

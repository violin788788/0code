from github import Github

# Load token from file

A:\Users\-\0code\git_token\git_token.txt

#with open("/home/info66/mysite/templates/token.txt", "r") as f:
with open(r"A:\Users\-\0code\git_token\git_token.txt", "r") as f:
    TOKEN = f.read().strip()  # remove whitespace

# Repo and branch
REPO = "violin788788/info"
BRANCH = "main"
#FILE = "/home/info66/mysite/templates/info.html"
FILE = "info.html"

# Connect to GitHub
g = Github(TOKEN)
repo = g.get_repo(REPO)

# Read HTML content
with open(FILE, "r") as f:
    content = f.read()

# Push to GitHub
try:
    existing = repo.get_contents("info.html", ref=BRANCH)
    repo.update_file("info.html", "Update info.html", content, existing.sha, branch=BRANCH)
    print("File updated on GitHub.")
except:
    repo.create_file("info.html", "Add info.html", content, branch=BRANCH)
    print("File created on GitHub.")

import subprocess

# Git identity (replace with yours)
subprocess.run(["git", "config", "user.name", "Your Name"])
subprocess.run(["git", "config", "user.email", "youremail@example.com"])

# Load token
with open(r"A:\Users\-\0code\git_token\git_token.txt", "r") as f:
    token = f.read().strip()

# Get changed files
changed_files = subprocess.check_output(["git", "status", "--porcelain"], text=True).splitlines()
files_to_add = [f.split()[-1] for f in changed_files if "." in f.split()[-1]]

if not files_to_add:
    print("No changed files with '.' to push.")
    exit()

# Stage only files with '.'
subprocess.run(["git", "add"] + files_to_add)

# Check if repo has any commits
try:
    subprocess.run(["git", "rev-parse", "HEAD"], check=True, stdout=subprocess.DEVNULL)
    has_commit = True
except subprocess.CalledProcessError:
    has_commit = False

# Commit
subprocess.run(["git", "commit", "-m", "Update files with dots"])

# Determine branch (default to main if no commits before)
try:
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
except subprocess.CalledProcessError:
    branch = "main"
    subprocess.run(["git", "branch", "-M", branch])

# Push using token
repo_url = f"https://{token}@github.com/violin788788/0code.git"
subprocess.run(["git", "push", "-u", repo_url, branch])

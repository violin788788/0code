import subprocess

# --- 1. Set Git identity (only affects this repo) ---
subprocess.run(["git", "config", "user.name", "Your Name"])
subprocess.run(["git", "config", "user.email", "youremail@example.com"])

# --- 2. Load GitHub token ---
with open(r"A:\Users\-\0code\git_token\git_token.txt", "r") as f:
    token = f.read().strip()

# --- 3. Get changed files ---
changed_files = subprocess.check_output(["git", "status", "--porcelain"], text=True).splitlines()
files_to_add = [f.split()[-1] for f in changed_files if "." in f.split()[-1]]

if not files_to_add:
    print("No changed files with '.' to push.")
    exit()

# --- 4. Stage only files with a dot ---
subprocess.run(["git", "add"] + files_to_add)

# --- 5. Commit ---
subprocess.run(["git", "commit", "-m", "Update files with dots"])

# --- 6. Detect branch or create 'main' ---
try:
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
except subprocess.CalledProcessError:
    branch = "main"
    subprocess.run(["git", "branch", "-M", branch])

# --- 7. Push to GitHub using token ---
repo_url = f"https://{token}@github.com/violin788788/0code.git"
subprocess.run(["git", "push", "-u", repo_url, branch])

print("Pushed all changed files with '.' to GitHub successfully!")



import os,subprocess


#"git push origin main --force"

# Define the Git commands
commands = [
    "git add -A",
    'git commit -m "Remove unwanted files and directories, and add/modify other changes"'
]

# Execute the commands in the shell using os.system()
for command in commands:
    os.system(command)


# Step 1: Read the token from the token.txt file
with open('token.txt', 'r') as file:
    token = file.read().strip()  # Read the token and remove any extra whitespace
# Step 2: Set up the GitHub repository URL with the token for authentication
repo_url = f"https://{token}@github.com/violin788788/info34.git"

# Step 3: Execute the Git command (force push)
try:
    # Run the git push command with the token for authentication
    subprocess.run(["git", "push", repo_url, "main", "--force"], check=True)
    print("Force push to GitHub was successful!")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")


    """
create git
git init

create main branch
git checkout -b main

add remote
git remote add origin https://github.com/violin788788/info34.git

stage all changes
git add -A

commit changes
git commit -m "Remove unwanted files and directories, and add/modify other changes"

force?
git push origin main --force

username
violin788788
token


remove tracking
git rm --cached .lesshst


"""
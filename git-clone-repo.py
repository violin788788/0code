import os
import subprocess
file_path = 'git-clone-repo.txt'
try:
    with open(file_path, 'r') as file:
        repo_name = file.read().strip().replace("\n", "").replace(" ", "")
    if not repo_name:
        print("The file is empty or does not contain a valid repo.")
    else:
        repo_url = f"https://github.com/{repo_name}.git"
        print(f"Cloning repository: {repo_url}")
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository {repo_url} has been cloned successfully.")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except subprocess.CalledProcessError:
    print("Failed to clone the repository. Please check the URL or your Git configuration.")
except Exception as e:
    print(f"An error occurred: {e}")

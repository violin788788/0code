import tkinter as tk
from tkinter import messagebox
import subprocess
import os
repos = ["info34", "vote34", "trading", "0code"]
def run_git_command(repo, command):
    repo_path = os.path.join(os.getcwd(), repo)
    if not os.path.isdir(repo_path):
        messagebox.showerror("Error", f"Repo {repo} not found!")
        return
    try:
        result = subprocess.run(f"git {command}", shell=True, cwd=repo_path, text=True, capture_output=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", f"{command} for {repo} completed successfully!")
        else:
            messagebox.showerror("Error", f"Error: {result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Error running git command: {e}")
def create_repo_buttons(root):
    for repo in repos:
        frame = tk.Frame(root)
        frame.pack(pady=10)
        label = tk.Label(frame, text=repo, width=20, anchor='w', font=("Arial", 16))  # Font size doubled
        label.pack(side="left")
        push_button = tk.Button(frame, text="git-push", command=lambda repo=repo: run_git_command(repo, "push"), font=("Arial", 16))
        push_button.pack(side="left", padx=5)
        pull_button = tk.Button(frame, text="git-pull", command=lambda repo=repo: run_git_command(repo, "pull"), font=("Arial", 16))
        pull_button.pack(side="left", padx=5)
def main():
    root = tk.Tk()
    root.title("Git Repo Manager")
    root.geometry("400x300")
    create_repo_buttons(root)
    root.mainloop()
if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
import os
def run_code():
    filename=code_input.get("1.0",tk.END).strip()
    if not filename:messagebox.showerror("Error","Please enter a filename");return
    if not filename.endswith(".py"):filename+=".py"
    if not os.path.exists(filename):messagebox.showerror("Error",f"File '{filename}' does not exist");return
    directory = r"A:\Users\-\0code\\"
    cmd = "python "+directory+filename
    print(cmd)
    os.system(cmd)
    #os.system(f"python \"{filename}\"")
root=tk.Tk()
root.title("Python Runner")
root.geometry("400x200")
tk.Label(root,text="Run what in Python?",font=("Arial",14)).pack(pady=10)
code_input=tk.Text(root,width=40,height=3,font=("Consolas",12))
code_input.pack(padx=10,pady=10)
run_button=tk.Button(root,text="Run",font=("Arial",12),command=run_code)
run_button.pack(pady=10)
root.mainloop()

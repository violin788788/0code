import tkinter as tk
from tkinter import scrolledtext,messagebox
import subprocess,tempfile,os
def run_code():
    code=code_input.get("1.0",tk.END)
    with tempfile.NamedTemporaryFile(delete=False,suffix=".py",mode="w",encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path=tmp.name
    try:
        result=subprocess.run(["python",tmp_path],capture_output=True,text=True)
        output=""
        if result.stdout:output+=f"Output:\n{result.stdout}\n"
        if result.stderr:output+=f"Errors:\n{result.stderr}"
        if not output:output="No output."
        messagebox.showinfo("Run Result",output)
    except Exception as e:messagebox.showerror("Error",str(e))
    finally:os.remove(tmp_path)
root=tk.Tk()
root.title("Python Runner")
root.geometry("200x600")
tk.Label(root,text="Run what in Python?",font=("Arial",14)).pack(pady=10)
code_input=scrolledtext.ScrolledText(root,width=70,height=20,font=("Consolas",12))
code_input.pack(padx=10,pady=10)
run_button=tk.Button(root,text="Run",font=("Arial",12),command=run_code)
run_button.pack(pady=10)
root.mainloop()

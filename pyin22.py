import os,shutil
TARGET_DIR=os.path.join(os.getcwd(),"screenshot")
os.makedirs(TARGET_DIR,exist_ok=True)
shutil.copy(__file__,os.path.join(TARGET_DIR,os.path.basename(__file__)))
print(f"Folder created at: {TARGET_DIR}")

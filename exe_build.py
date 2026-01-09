import PyInstaller.__main__
import shutil, os,sys

def generate_onedir(file_name):
    #file_name = "screenshot"
    file_extension = ".py"
    icon_name = file_name + ".ico"
    script = file_name + file_extension
    PyInstaller.__main__.run([script,'--onedir','--name=' + file_name,'--icon=' + icon_name,'--windowed'])
    dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
    os.startfile(dist_folder)

def generate_onefile(file_name):
    file_extension = ".py"
    icon_name = file_name + ".ico"
    script = file_name + file_extension
    out_name = file_name+"-installer"
    PyInstaller.__main__.run([script,'--onefile','--name=' + out_name,'--icon=' + icon_name,'--windowed'])
    dist_folder = os.path.join(os.getcwd(), 'dist', out_name)
    os.startfile(dist_folder)

file_name = "run"

file=file_name+".py"
ico = file_name+".ico"
#command = "pyinstaller --onefile --icon="+ico+" "+file
command = "pyinstaller --onefile --icon="+ico+" "+file
os.system(command)
#file_name = "record"
generate_onedir(file_name)
#copy to program files

cwd = os.getcwd()
drive = os.path.splitdrive(os.getcwd())[0]+"\\"
src = os.path.join(cwd, "dist", file_name)+".exe"
dst = os.path.join(drive, "Program Files", file_name)+".exe"

try:
    shutil.copy2(src, dst)
    print(f"Copied {src} -> {dst}")
except PermissionError:
    print("Permission denied: run as Administrator")
except FileNotFoundError:
    print(f"File not found: {src}")
print("exe copied to program files")


#os.startfile("dist")
import PyInstaller.__main__
import shutil, os,sys
"""
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
"""


file_without_py = "run"
#onefile_or_onedir = "onedir"
onefile_or_onedir = "onefile"


if ".py" not in file_without_py:
    file_with_py=file_without_py+".py"
cwd = os.getcwd()
ico_name = file_without_py+".ico"
ico_directory = os.path.join(cwd,"icos")
ico = os.path.join(ico_directory,ico_name)
#command = "pyinstaller --onefile --icon="+ico+" "+file
#will throw error if file_with_py not have .py in it ..
command = "pyinstaller --"+onefile_or_onedir+" --icon="+ico+" "+file_with_py
os.system(command)
#file_name = "record"
#generate_onedir(file_name)
#copy to program files
cwd = os.getcwd()
drive = os.path.splitdrive(os.getcwd())[0]+"\\"
exe_file = file_without_py+".exe"
#..change this to cwd drive..etc..

cwd = os.getcwd()

code_directory = cwd

src=os.path.join(code_directory,"dist",exe_file)
dst = os.path.join(drive, "Program Files", exe_file)
shutil.copy2(src, dst)
os.startfile("dist")
os.startfile(os.path.join(drive, "Program Files"))
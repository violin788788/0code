import PyInstaller.__main__
import os

def generate_onedir(file_name):
    #file_name = "screenshot"
    file_extension = ".py"
    icon_name = file_name + ".ico"
    script = file_name + file_extension
    PyInstaller.__main__.run([script,'--onedir','--name=' + file_name,'--icon=' + icon_name,'--windowed'])
    dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
    os.startfile(dist_folder)

file_name = "screenshot"
generate_onedir(file_name)


def generate_onefile(file_name):
    file_extension = ".py"
    icon_name = file_name + ".ico"
    script = file_name + file_extension
    out_name = file_name+"-installer"
    PyInstaller.__main__.run([script,'--onefile','--name=' + out_name,'--icon=' + icon_name,'--windowed'])
    dist_folder = os.path.join(os.getcwd(), 'dist', out_name)
    os.startfile(dist_folder)

file_name = "screenshot"
generate_onefile(file_name)
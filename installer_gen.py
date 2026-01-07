import os
import shutil
import sys
import PyInstaller.__main__
def generate_onedir(file_name):
    file_extension = ".py"
    icon_name = file_name + ".ico"
    script = file_name + file_extension
    PyInstaller.__main__.run([script, '--onedir', '--name=' + file_name, '--icon=' + icon_name, '--windowed'])
    dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
    os.startfile(dist_folder)
def generate_installer_exe(file_name):
    dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
    if not os.path.exists(dist_folder):
        print(f"Error: {dist_folder} not found!")
        sys.exit(1)
    drive = os.path.splitdrive(os.path.abspath(sys.executable))[0]
    program_files = os.path.join(drive + '\\', 'Program Files', file_name)
    if os.path.exists(program_files):
        shutil.rmtree(program_files)  # Remove old folder if exists
    shutil.copytree(dist_folder, program_files)  # Copy the entire screenshot folder
    print(f"Installed {file_name} to {program_files}")
file_name = "screenshot"
generate_onedir(file_name)
generate_installer_exe(file_name)

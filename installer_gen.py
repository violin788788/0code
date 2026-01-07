import PyInstaller.__main__
import os
import shutil
import sys
import tempfile
import zipfile
file_name = "screenshot"
file_extension = ".py"
icon_name = file_name + ".ico"
script = file_name + file_extension
PyInstaller.__main__.run([script, '--onedir', '--name=' + file_name, '--icon=' + icon_name, '--windowed'])
dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
os.startfile(dist_folder)
zip_path = os.path.join(os.getcwd(), 'screenshot.zip')
shutil.make_archive(zip_path.replace('.zip', ''), 'zip', dist_folder)
drive = os.path.splitdrive(os.path.abspath(sys.executable))[0]
program_files = os.path.join(drive + '\\', 'Program Files', file_name)
tmp = tempfile.mkdtemp()
zip_path_in_exe = os.path.join(getattr(sys, '_MEIPASS', '.'), 'screenshot.zip')
with zipfile.ZipFile(zip_path_in_exe, 'r') as zip_ref:
    zip_ref.extractall(tmp)
if os.path.exists(program_files):
    shutil.rmtree(program_files)
shutil.copytree(os.path.join(tmp, file_name), program_files)
shutil.rmtree(tmp)
print(f"Installed {file_name} to {program_files}")

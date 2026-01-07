import PyInstaller.__main__
import os
file_name = "screenshot"
file_extension = ".py"
icon_name = file_name + ".ico"
script = file_name + file_extension
PyInstaller.__main__.run([script,'--onedir','--name=' + file_name,'--icon=' + icon_name,'--windowed'])
dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
os.startfile(dist_folder)

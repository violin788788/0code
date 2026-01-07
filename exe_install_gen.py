import PyInstaller.__main__
import sys
import os

# Set the script and icon directly
script_path = 'screenshot.pyw'
icon_path = 'screenshot.ico'

# Generate output name with _installer
base_name = os.path.splitext(os.path.basename(script_path))[0] + "_installer"

PyInstaller.__main__.run([
    script_path,
    '--onedir',            # create folder with files
    '--name=' + base_name,
    '--icon=' + icon_path,
    '--windowed'           # GUI app, no console
])

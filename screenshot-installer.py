

import os
import shutil
import sys
def install_screenshot(file_name):
    dist_folder = os.path.join(os.getcwd(), 'dist', file_name)
    drive = os.path.splitdrive(os.path.abspath(sys.executable))[0]
    program_files = os.path.join(drive + '\\', 'Program Files', file_name)
    if not os.path.exists(dist_folder):
        print(f"Error: {dist_folder} not found!")
        sys.exit(1)
    if os.path.exists(program_files):
        shutil.rmtree(program_files)
    shutil.copytree(dist_folder, program_files)
    print(f"Installed screenshot to {program_files}")


install_screenshot('screenshot')

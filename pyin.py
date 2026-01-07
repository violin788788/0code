import subprocess

PY_FILE = "screenshot.pyw"
ICON_FILE = "screenshot.ico"
EXE_NAME = "screenshot_installer"  # original name + "_installer"

try:
    subprocess.run([
        "pyinstaller",
        "--onefile",
        f"--icon={ICON_FILE}",
        "--name",
        EXE_NAME,
        PY_FILE
    ], check=True)
    print("EXE created successfully!")
except subprocess.CalledProcessError as e:
    print("Error:", e)

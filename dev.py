import os

cwd = os.getcwd()
val = os.path.splitdrive(cwd)
drive = val[0]
print(val)
print(drive)
#drive, _ = os.path.splitdrive(cwd)

#print(drive)  # This will print the drive, e.g., "C:", "D:", etc.

#print(str(drive)+"--")
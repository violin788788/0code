import os
import getpass

# Get the system drive (Windows) or root directory (macOS/Linux)
if os.name == 'nt':  # Windows
    drive = os.getenv('SystemDrive')  # e.g., 'C:'
else:  # macOS/Linux
    drive = '/'  # Root directory

# Get the current logged-in user
user = getpass.getuser()  # This works on Windows, macOS, Linux

# Print the results
print(f"Drive: {drive}")
print(f"User: {user}")


pathjoin

drive    Users    user   Downloads




import os

# Example parts
drive = "C:"  # For Windows, this is the system drive (you can replace it with any other drive letter)
users_folder = "Users"
user_name = "JohnDoe"  # Replace with the actual user name
downloads_folder = "Downloads"

# Create the full path using os.path.join
full_path = os.path.join(drive, users_folder, user_name, downloads_folder)

# Print the result
print("Full path:", full_path)


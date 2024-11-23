import os
from PyInstaller.__main__ import run

# Define the Python script content
script_content = """
def main():
    print("Hello, this is a simple script with an embedded icon resource.")

if __name__ == "__main__":
    main()
"""

# Write the script content to a file
script_filename = 'simple_script.py'
with open(script_filename, 'w') as file:
    file.write(script_content)

# Path to the icon file
icon_path = 'app_icon.ico'

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PyInstaller command to bundle the script into a single executable with an icon
pyinstaller_command = [
    '--onefile',  # Create a single executable file
    f'--icon={icon_path}',  # Specify the path to the icon file
    f'--distpath=./tmp/',  # Specify the output directory for the executable
    script_filename,  # The Python script to convert into an executable
]

# Run PyInstaller with the specified command
run(pyinstaller_command)

# Clean up by removing the temporary Python script file
os.remove(script_filename)

# Reminder: Make sure PyInstaller is installed in your environment
# You can install it using pip:
# pip install pyinstaller
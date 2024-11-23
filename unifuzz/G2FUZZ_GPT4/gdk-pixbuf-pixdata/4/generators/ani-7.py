import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Path to the new .ani file
ani_file_path = './tmp/compatibility.ani'

# Basic content to include in the .ani file
ani_content = """
[Info]
Name=CompatibilityDemo
Author=YourName
Compatibility=Windows

This is a basic .ani file created to demonstrate generating an .ani file with Python.
It's intended to reflect the feature of compatibility with Windows platforms.
"""

# Writing the content to the .ani file
with open(ani_file_path, 'w') as file:
    file.write(ani_content)

print(f"ANI file created at {ani_file_path}")
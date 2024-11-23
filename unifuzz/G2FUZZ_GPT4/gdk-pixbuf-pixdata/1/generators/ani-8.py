import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# ANI file header and content placeholders
ani_header = "RIFF....ACONanih....rate....seq ...."
ani_content = """
8. **Compatibility and Support**: Primarily supported by the Microsoft Windows operating system, ANI files are widely used for customizing cursor themes and enhancing user interface interactivity. However, compatibility might be limited on non-Windows platforms without specialized software.
"""

# Combine header and content to simulate an ANI file structure
ani_file_data = ani_header + ani_content

# Path to save the file
file_path = './tmp/feature_description.ani'

# Write the data to an ANI file
with open(file_path, 'w') as file:
    file.write(ani_file_data)

print(f"File saved to {file_path}")
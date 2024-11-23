import zipfile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The name of the zip file to create
zip_filename = './tmp/cross_platform_compatibility.zip'

# The content to include in the text file inside the zip
content = """Cross-Platform Compatibility:
ZIP files are supported on various operating systems, including Windows, macOS, and Linux, ensuring wide usability and accessibility."""

# The name of the text file to be included in the zip
text_filename = 'cross_platform_compatibility.txt'

# Creating a zip file and writing the text file with the content
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.writestr(text_filename, content)

print(f"ZIP file '{zip_filename}' has been created successfully.")
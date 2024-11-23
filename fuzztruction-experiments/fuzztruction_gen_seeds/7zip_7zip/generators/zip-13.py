import zipfile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The name of the zip file to create
zip_filename = './tmp/advanced_features.zip'

# The content to include in the text files inside the zip
content = """Cross-Platform Compatibility:
ZIP files are supported on various operating systems, including Windows, macOS, and Linux, ensuring wide usability and accessibility."""

central_directory_structure_content = """Central Directory Structure:
The central directory at the end of a ZIP file lists all the files in the archive, including their metadata, making file access efficient without needing to read the entire archive."""

# The names of the text files to be included in the zip
text_filename = 'cross_platform_compatibility.txt'
central_directory_filename = 'central_directory_structure.txt'

# Creating a zip file and writing the text files with the content
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.writestr(text_filename, content)
    zipf.writestr(central_directory_filename, central_directory_structure_content)

print(f"ZIP file '{zip_filename}' has been created successfully with the additional feature.")
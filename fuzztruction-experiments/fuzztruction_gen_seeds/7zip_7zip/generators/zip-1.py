import zipfile
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# The content to be written
content = """
Compression: ZIP files can compress data using various algorithms, significantly reducing the size of files and folders for storage or transmission.
"""

# The path for the zip file
zip_path = './tmp/compression_demo.zip'

# Creating a zip file in write mode
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Writing content to a file inside the zip
    zipf.writestr('compression_info.txt', content)
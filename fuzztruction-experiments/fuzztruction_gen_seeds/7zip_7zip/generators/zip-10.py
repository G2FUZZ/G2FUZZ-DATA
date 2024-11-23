import zipfile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new ZIP file and add a comment
zip_filename = './tmp/archive_with_comment.zip'
with zipfile.ZipFile(zip_filename, 'w') as myzip:
    myzip.comment = b'This is a comment that can be read without decompressing the archive.'

print(f'ZIP file created with comment: {zip_filename}')
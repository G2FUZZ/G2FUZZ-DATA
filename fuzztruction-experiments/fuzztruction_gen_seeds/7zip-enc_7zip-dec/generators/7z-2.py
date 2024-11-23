import py7zr
from py7zr import pack_7zarchive, unpack_7zarchive
import shutil
import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Define the archive name and the password for encryption
archive_name = os.path.join(tmp_dir, 'encrypted.7z')
password = 'your_password_here'

# Create a small text file to include in the archive
# This is to demonstrate adding a file, as an entirely empty encrypted archive might not be practical
text_content = "This is a test file."
text_file_path = os.path.join(tmp_dir, 'test_file.txt')
with open(text_file_path, 'w') as f:
    f.write(text_content)

# Register the 7z format with optional encryption
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# Create an encrypted 7z file
with py7zr.SevenZipFile(archive_name, 'w', password=password) as archive:
    archive.writeall(tmp_dir, 'base')

# Cleanup by removing the temporary text file (optional)
os.remove(text_file_path)
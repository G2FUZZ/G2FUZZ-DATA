import py7zr
import shutil
import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Define the archive name and the password for encryption
archive_name = os.path.join(tmp_dir, 'encrypted.7z')
password = 'your_password_here'

# Create a small text file to include in the archive
text_content = "This is a test file."
text_file_path = os.path.join(tmp_dir, 'test_file.txt')
with open(text_file_path, 'w') as f:
    f.write(text_content)

# Function to pack files into a 7z archive
def pack_7zarchive(name, base_dir, **kwargs):
    with py7zr.SevenZipFile(name, 'w', password=password) as archive:
        archive.writeall(base_dir, 'base')

# Function to unpack a 7z archive
def unpack_7zarchive(filename, extract_dir):
    with py7zr.SevenZipFile(filename, mode='r', password=password) as z:
        z.extractall(path=extract_dir)

# Register the 7z format with optional encryption
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# Define the dictionary size for compression (in bytes)
# Example: 16MB dictionary size
dictionary_size = 16 * 1024 * 1024

# Create an encrypted 7z file with adjustable dictionary size
with py7zr.SevenZipFile(archive_name, 'w', password=password, filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9, 'dict_size': dictionary_size}]) as archive:
    archive.writeall(tmp_dir, 'base')

# Cleanup by removing the temporary text file (optional)
os.remove(text_file_path)
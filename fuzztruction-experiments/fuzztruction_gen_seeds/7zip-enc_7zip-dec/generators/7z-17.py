import py7zr
import shutil
import os

def pack_7zarchive(name, base_dir, password=None):
    """
    Create a 7z archive.

    :param name: The name of the file to create, including the path, minus any format-specific extension.
    :param base_dir: Directory to archive.
    :param password: Password for encrypting the archive.
    """
    archive_name = f"{name}.7z"
    with py7zr.SevenZipFile(archive_name, 'w', password=password) as archive:
        archive.writeall(base_dir, arcname=os.path.basename(base_dir))

def unpack_7zarchive(filename, extract_dir):
    """
    Unpack a 7z archive.

    :param filename: The path to the archive.
    :param extract_dir: The directory to extract the archive into.
    """
    with py7zr.SevenZipFile(filename, mode='r') as z:
        z.extractall(path=extract_dir)

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Define the archive name and the password for encryption
archive_name = os.path.join(tmp_dir, 'encrypted')
password = 'your_password_here'

# Create a small text file to include in the archive
text_content = "This is a test file."
text_file_path = os.path.join(tmp_dir, 'test_file.txt')
with open(text_file_path, 'w') as f:
    f.write(text_content)

# Register the 7z format with optional encryption
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# Create an encrypted 7z file
pack_7zarchive(archive_name, tmp_dir, password=password)

# Cleanup by removing the temporary text file (optional)
os.remove(text_file_path)
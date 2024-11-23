import py7zr
import shutil
import os

def pack_7zarchive(name, base_dir, password=None, compression_level=5):
    """
    Create a 7z archive with adjustable compression level.

    :param name: The name of the file to create, including the path, minus any format-specific extension.
    :param base_dir: Directory to archive.
    :param password: Password for encrypting the archive.
    :param compression_level: Compression level (1-9), 1 is fastest, 9 is maximum compression.
    """
    archive_name = f"{name}.7z"
    compression = {'level': compression_level}
    with py7zr.SevenZipFile(archive_name, 'w', password=password, filters=[{'id': py7zr.FILTER_LZMA2, 'preset': compression_level}]) as archive:
        archive.writeall(base_dir, arcname=os.path.basename(base_dir))

def unpack_7zarchive(filename, extract_dir, speed_mode=False):
    """
    Unpack a 7z archive.

    :param filename: The path to the archive.
    :param extract_dir: The directory to extract the archive into.
    :param speed_mode: If True, use speed optimized settings for decompression (might not be effective for all archives).
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
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive with compression speed options')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# Create an encrypted 7z file with custom compression level
compression_level = 9  # Maximum compression
pack_7zarchive(archive_name, tmp_dir, password=password, compression_level=compression_level)

# Cleanup by removing the temporary text file (optional)
os.remove(text_file_path)
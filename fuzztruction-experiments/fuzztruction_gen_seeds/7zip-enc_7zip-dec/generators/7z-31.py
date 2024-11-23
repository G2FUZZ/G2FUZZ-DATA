import py7zr
import shutil
import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Define the archive name and the password for encryption
archive_name = os.path.join(tmp_dir, 'encrypted_with_extensible_format.7z')
password = 'your_password_here'

# Create a small text file to include in the archive
text_content = "This is a test file."
text_file_path = os.path.join(tmp_dir, 'test_file.txt')
with open(text_file_path, 'w') as f:
    f.write(text_content)

# Create an additional text file to describe the Extensible format feature
extensible_format_desc = """Extensible format: The 7z format is designed to be extensible, meaning new features and improvements can be added over time without compromising compatibility with older versions of the software."""
extensible_format_file_path = os.path.join(tmp_dir, 'extensible_format.txt')
with open(extensible_format_file_path, 'w') as f:
    f.write(extensible_format_desc)

# Create a new text file to describe the SFX modules customization feature
sfx_customization_desc = """SFX modules customization: For self-extracting archives, users can customize the SFX module, altering aspects like the extraction path or the inclusion of a license agreement before extraction."""
sfx_customization_file_path = os.path.join(tmp_dir, 'sfx_customization.txt')
with open(sfx_customization_file_path, 'w') as f:
    f.write(sfx_customization_desc)

# Function to pack files into a 7z archive
def pack_7zarchive(name, base_dir, **kwargs):
    with py7zr.SevenZipFile(name, 'w', password=password) as archive:
        archive.writeall(base_dir, 'base')

# Function to unpack a 7z archive
def unpack_7zarchive(filename, extract_dir):
    with py7zr.SevenZipFile(filename, mode='r', password=password) as z:
        z.extractall(path=extract_dir)

# Register the 7z format with optional encryption
shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive with extensible format')
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

# Define the dictionary size for compression (in bytes)
# Example: 16MB dictionary size
dictionary_size = 16 * 1024 * 1024

# Create an encrypted 7z file with adjustable dictionary size and including the extensible format description and the SFX modules customization
with py7zr.SevenZipFile(archive_name, 'w', password=password, filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9, 'dict_size': dictionary_size}]) as archive:
    archive.writeall(tmp_dir, 'base')

# Cleanup by removing the temporary files (optional)
os.remove(text_file_path)
os.remove(extensible_format_file_path)
os.remove(sfx_customization_file_path)
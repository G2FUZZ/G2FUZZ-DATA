import os
from py7zr import SevenZipFile

# Directory where the 7z file will be saved
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

# Path for the 7z file to be created
archive_path = os.path.join(output_dir, 'example.7z')

# Create a 7z archive with the specified path
with SevenZipFile(archive_path, 'w') as archive:
    # Normally, you would add files here using archive.writeall() or similar methods
    pass  # Placeholder for adding files to the archive

print(f'7z archive created at {archive_path}')
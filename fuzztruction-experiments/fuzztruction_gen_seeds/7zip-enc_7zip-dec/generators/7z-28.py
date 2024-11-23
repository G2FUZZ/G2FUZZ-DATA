import os
from py7zr import SevenZipFile

# Directory where the 7z file will be saved
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

# Path for the 7z file to be created
archive_path = os.path.join(output_dir, 'example_with_chaining.7z')

# Define a sequence of compression methods to apply
compression_methods = [
    {"id": "lzma2", "preset": 9},  # First, apply LZMA2 with the highest compression level
    {"id": "bcj", "preset": None}  # Then apply BCJ (Branch Call Jump) transformation without any preset
]

# Create a 7z archive with the specified path and compression method chaining
with SevenZipFile(archive_path, 'w', filters=compression_methods) as archive:
    # Normally, you would add files here using archive.writeall() or similar methods
    pass  # Placeholder for adding files to the archive

print(f'7z archive created with compression method chaining at {archive_path}')
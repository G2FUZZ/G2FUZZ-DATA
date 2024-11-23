import os
from py7zr import pack_7zarchive, unpack_7zarchive
import shutil

# Register the format for both packing and unpacking
shutil.register_archive_format('7z', pack_7zarchive, description='7z archive')
shutil.register_unpack_format('7z', ['.7z'], unpack_7zarchive)

# Content to be written
content = "12. Open architecture: The 7z format is open-source, allowing developers to integrate its support into their applications without licensing fees."

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Temporary file path
temp_file_path = './tmp/feature.txt'

# The target 7z file path
archive_path = './tmp/feature_description.7z'

# Write the content to a temporary file
with open(temp_file_path, 'w') as file:
    file.write(content)

# Create a 7z file containing the temporary file
shutil.make_archive(archive_path[:-3], '7z', root_dir='./tmp/', base_dir='feature.txt')

# Clean up the temporary file
os.remove(temp_file_path)
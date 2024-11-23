import os
from py7zr import pack_7zarchive, unpack_7zarchive
import shutil

# Register the format for both packing and unpacking
shutil.register_archive_format('7z', pack_7zarchive, description='7z archive')
shutil.register_unpack_format('7z', ['.7z'], unpack_7zarchive)

# Content to be written for the first feature
content_open_architecture = "12. Open architecture: The 7z format is open-source, allowing developers to integrate its support into their applications without licensing fees."

# Content for the new feature
content_environmentally_adaptive = "4. Environmentally adaptive: The 7z format's performance and efficiency can vary based on the system's hardware and software environment, making it adaptable to different configurations for optimal results."

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Temporary file paths
temp_file_path_open_architecture = './tmp/feature_open_architecture.txt'
temp_file_path_environmentally_adaptive = './tmp/feature_environmentally_adaptive.txt'

# The target 7z file path
archive_path = './tmp/feature_descriptions.7z'

# Write the content to a temporary file for the first feature
with open(temp_file_path_open_architecture, 'w') as file:
    file.write(content_open_architecture)

# Write the content to a second temporary file for the new feature
with open(temp_file_path_environmentally_adaptive, 'w') as file:
    file.write(content_environmentally_adaptive)

# Create a 7z file containing both temporary files
shutil.make_archive(archive_path[:-3], '7z', root_dir='./tmp/', base_dir='.')

# Optionally, clean up the temporary files
# os.remove(temp_file_path_open_architecture)
# os.remove(temp_file_path_environmentally_adaptive)
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

# Content for the File filtering feature
content_file_filtering = "8. File filtering: When creating or extracting archives, users can specify patterns to include or exclude specific files or directories, providing greater control over the archive's contents."

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Temporary file paths
temp_file_path_open_architecture = './tmp/feature_open_architecture.txt'
temp_file_path_environmentally_adaptive = './tmp/feature_environmentally_adaptive.txt'
temp_file_path_file_filtering = './tmp/feature_file_filtering.txt'  # Path for the new feature file

# The target 7z file path
archive_path = './tmp/feature_descriptions.7z'

# Write the content to a temporary file for the first feature
with open(temp_file_path_open_architecture, 'w') as file:
    file.write(content_open_architecture)

# Write the content to a second temporary file for the new feature
with open(temp_file_path_environmentally_adaptive, 'w') as file:
    file.write(content_environmentally_adaptive)

# Write the content to a third temporary file for the File filtering feature
with open(temp_file_path_file_filtering, 'w') as file:
    file.write(content_file_filtering)

# Create a 7z file containing all three temporary files
shutil.make_archive(archive_path[:-3], '7z', root_dir='./tmp/', base_dir='.')

# Optionally, clean up the temporary files
# os.remove(temp_file_path_open_architecture)
# os.remove(temp_file_path_environmentally_adaptive)
# os.remove(temp_file_path_file_filtering)
import os
from py7zr import SevenZipFile

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Creating a sample file
sample_file_path = os.path.join(output_dir, 'sample.txt')
with open(sample_file_path, 'wb') as f:
    f.write(b"This is a sample content to demonstrate 7z archives." * 100)  # Adjust content size as needed

# Creating a Plugin Support description file
plugin_support_path = os.path.join(output_dir, 'plugin_support.txt')
with open(plugin_support_path, 'w') as f:
    f.write("Plugin support: Some versions of 7z and software that can handle 7z files support plugins, "
            "which can extend the functionality of the software, including support for additional file formats "
            "or compression methods.")

# Archive name
archive_name = os.path.join(output_dir, "archive_with_plugin_support.7z")

# Creating the archive with the additional Plugin Support file
with SevenZipFile(archive_name, 'w') as archive:
    archive.writeall(output_dir, "base_dir")

print(f"7z archive with plugin support feature created at {archive_name}.")
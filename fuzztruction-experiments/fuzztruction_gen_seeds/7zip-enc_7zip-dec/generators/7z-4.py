import os
from py7zr import SevenZipFile

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Creating a sample file
sample_file_path = os.path.join(output_dir, 'sample.txt')
with open(sample_file_path, 'wb') as f:
    f.write(b"This is a sample content to demonstrate 7z archives." * 100)  # Adjust content size as needed

# Archive name
archive_name = os.path.join(output_dir, "archive.7z")

# Creating the archive
with SevenZipFile(archive_name, 'w') as archive:
    archive.writeall(output_dir, "base_dir")

print(f"7z archive created at {archive_name}.")
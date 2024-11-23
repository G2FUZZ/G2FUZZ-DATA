import py7zr
import os

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Sample data to compress - creating a few sample files in memory
files_content = {
    "file1.txt": "This is the content of file 1.",
    "file2.txt": "This is the content of file 2, similar to file 1.",
    "file3.txt": "This is the content of file 3, also similar, to demonstrate solid compression."
}

# Specify the archive name
archive_name = os.path.join(output_dir, "solid_compression.7z")

# Create a 7z archive
with py7zr.SevenZipFile(archive_name, 'w') as archive:
    for filename, content in files_content.items():
        archive.writestr(filename, content)

print(f"7z archive created at: {archive_name}")
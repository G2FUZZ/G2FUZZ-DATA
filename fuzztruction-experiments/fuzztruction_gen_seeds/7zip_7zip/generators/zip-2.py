import os
from zipfile import ZipFile

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the name of the zip file
zip_file_path = './tmp/multiple_files_folders.zip'

# Create a zip file
with ZipFile(zip_file_path, 'w') as zipf:
    # Create files and folders structure in memory and write them to the zip
    # Folder 1 with two files
    zipf.writestr('Folder1/file1.txt', 'This is the content of file1 in Folder1.')
    zipf.writestr('Folder1/file2.txt', 'This is the content of file2 in Folder1.')
    
    # Folder 2 with two files
    zipf.writestr('Folder2/file1.txt', 'This is the content of file1 in Folder2.')
    zipf.writestr('Folder2/file2.txt', 'This is the content of file2 in Folder2.')

print(f'ZIP file with multiple files and folders has been created at {zip_file_path}')
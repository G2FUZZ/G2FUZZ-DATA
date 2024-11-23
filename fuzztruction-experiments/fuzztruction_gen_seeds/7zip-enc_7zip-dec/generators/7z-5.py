import os
import shutil  # Corrected import
from py7zr import pack_7zarchive  # Only import pack_7zarchive from py7zr

def create_directory_structure(base_path):
    os.makedirs(base_path, exist_ok=True)
    directories = ['dir1', 'dir2']
    files = {
        'dir1': ['file1.txt', 'file2.txt'],
        'dir2': ['file3.txt', 'file4.txt']
    }

    for dir_name in directories:
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        for file_name in files[dir_name]:
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'w') as f:
                f.write(f"This is the content of {file_name}.\n")

if __name__ == "__main__":
    base_path = './tmp/'
    archive_name = os.path.join(base_path, 'filesystem_support.7z')

    # Create a temporary directory structure with files
    create_directory_structure(base_path)

    # Register the 7z format for use with shutil
    shutil.register_archive_format('7z', pack_7zarchive, description='7z archive')

    # Compress the directory structure into a 7z file
    shutil.make_archive(archive_name[:-3], '7z', base_path)

    print(f"7z archive created at: {archive_name}")
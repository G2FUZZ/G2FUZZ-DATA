import os
import shutil

# Define the source file path
source_file = "path/to/source/file.txt"

# Define the destination directory path
destination_directory = "./tmp/"

# Check if the source file exists
if os.path.exists(source_file):
    # Copy the source file to the destination directory
    shutil.copy(source_file, destination_directory)
    print("File copied successfully.")
else:
    print("Source file not found.")
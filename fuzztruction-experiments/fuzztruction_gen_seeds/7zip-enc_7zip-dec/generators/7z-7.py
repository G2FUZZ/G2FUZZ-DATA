import os
import tempfile
import py7zr  # Corrected import

# Create the directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define a list of filenames with Unicode characters
unicode_filenames = [
    "こんにちは.txt",  # Japanese for "Hello"
    "привет.txt",     # Russian for "Hello"
    "你好.txt"         # Chinese for "Hello"
]

# Create a temporary directory to hold the files before archiving
with tempfile.TemporaryDirectory() as temp_dir:
    # Create each file with Unicode names in the temp directory
    for filename in unicode_filenames:
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("This is a test file named " + filename)
    
    # Create a 7z archive with the Unicode filenames
    archive_path = os.path.join(output_dir, 'unicode_filenames.7z')
    with py7zr.SevenZipFile(archive_path, mode='w') as archive:  # Corrected usage
        for filename in unicode_filenames:
            file_path = os.path.join(temp_dir, filename)
            archive.writeall(temp_dir, arcname=filename)
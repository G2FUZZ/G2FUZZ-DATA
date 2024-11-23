import os
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED
import pyminizip

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filenames and password
zip_filename = './tmp/protected_zip.zip'
exe_filename = './tmp/protected_zip.exe'  # Name for the self-extracting archive
password = 'secure_password'

# Create a sample file to include in the zip
sample_filename = './tmp/sample.txt'
with open(sample_filename, 'w') as sample_file:
    sample_file.write('This is a sample file to be zipped and password protected.')

# Using pyminizip to create a password-protected zip
compression_level = 5  # Compression level: 1-9
pyminizip.compress(sample_filename, None, zip_filename, password, compression_level)

# Cleanup the sample file
os.remove(sample_filename)

# Convert the ZIP to a self-extracting archive (SFX)
# This step requires the 7-Zip command line tool (7z) to be installed and accessible from the command line

# For Windows
sfx_command = f'copy /b "C:\\Program Files\\7-Zip\\7zS.sfx" + config.txt + "{zip_filename}" "{exe_filename}"'
# For Linux or macOS, the command might slightly differ, e.g.,
# sfx_command = f'cat /usr/lib/p7zip/7z.sfx "{zip_filename}" > "{exe_filename}"'

# Execute the command to create the self-extracting archive
os.system(sfx_command)

print(f"Password-protected self-extracting archive created at: {exe_filename}")
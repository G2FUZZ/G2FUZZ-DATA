import os
from zipfile import ZipFile, ZIP_DEFLATED
from zipfile import PyZipFile
import pyminizip

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename and password
zip_filename = './tmp/protected_zip.zip'
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

print(f"Password-protected zip file created at: {zip_filename}")
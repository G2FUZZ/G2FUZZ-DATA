import os
from py7zr import SevenZipFile, FILTER_LZMA2

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Archive file path
archive_path = './tmp/encrypted_header.7z'

# Password for encryption
password = 'your_password_here'

# Create an encrypted 7z archive with encrypted headers
with SevenZipFile(archive_path, 'w', password=password) as archive:
    archive.set_encrypted_header(True)  # Enable header encryption
    # Since there's no input file mentioned, we won't add any files to the archive

print(f'Encrypted 7z archive with header encryption has been created at {archive_path}')
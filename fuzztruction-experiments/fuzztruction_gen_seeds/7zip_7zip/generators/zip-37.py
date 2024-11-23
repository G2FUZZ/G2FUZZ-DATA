import os
import hashlib
from zipfile import ZipFile
import time

# Function to create a SHA-256 checksum of a file
def create_sha256_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Create a temporary directory to hold files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Path for the files
signature_file_path = os.path.join(tmp_dir, 'digital_signature.txt')
incremental_backup_info_path = os.path.join(tmp_dir, 'incremental_backup_info.txt')
checksums_file_path = os.path.join(tmp_dir, 'checksums.txt')
zip_file_path = os.path.join(tmp_dir, 'signed_document_with_incremental_backup_and_checksum.zip')

# Create a dummy digital signature file
with open(signature_file_path, 'w') as signature_file:
    signature_file.write('This is a dummy digital signature.')

# Simulate creating an incremental backup info file
with open(incremental_backup_info_path, 'w') as incremental_backup_file:
    incremental_backup_file.write('Backup created on: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    incremental_backup_file.write('Description: Only files changed since the last backup are included.')

# Create a checksums file for integrity verification
checksums = {
    'digital_signature.txt': create_sha256_checksum(signature_file_path),
    'incremental_backup_info.txt': create_sha256_checksum(incremental_backup_info_path),
}

with open(checksums_file_path, 'w') as checksums_file:
    for file, checksum in checksums.items():
        checksums_file.write(f'{file}: {checksum}\n')

# Create a ZIP file and add the digital signature file, incremental backup info, and checksums for integrity verification
with ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(signature_file_path, arcname='digital_signature.txt')
    zipf.write(incremental_backup_info_path, arcname='incremental_backup_info.txt')
    zipf.write(checksums_file_path, arcname='checksums.txt')

print(f'ZIP file with digital signature, incremental backup support, and checksums for integrity verification created at: {zip_file_path}')
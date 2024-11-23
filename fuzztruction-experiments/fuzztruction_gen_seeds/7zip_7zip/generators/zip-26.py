import os
from zipfile import ZipFile
import time

# Create a temporary directory to hold files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Path for the files
signature_file_path = os.path.join(tmp_dir, 'digital_signature.txt')
incremental_backup_info_path = os.path.join(tmp_dir, 'incremental_backup_info.txt')
zip_file_path = os.path.join(tmp_dir, 'signed_document_with_incremental_backup.zip')

# Create a dummy digital signature file
with open(signature_file_path, 'w') as signature_file:
    signature_file.write('This is a dummy digital signature.')

# Simulate creating an incremental backup info file
with open(incremental_backup_info_path, 'w') as incremental_backup_file:
    incremental_backup_file.write('Backup created on: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    incremental_backup_file.write('Description: Only files changed since the last backup are included.')

# Create a ZIP file and add the digital signature file and incremental backup info
with ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(signature_file_path, arcname='digital_signature.txt')
    zipf.write(incremental_backup_info_path, arcname='incremental_backup_info.txt')

print(f'ZIP file with digital signature and incremental backup support created at: {zip_file_path}')
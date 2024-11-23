import os
from zipfile import ZipFile

# Create a temporary directory to hold files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Path for the files
signature_file_path = os.path.join(tmp_dir, 'digital_signature.txt')
zip_file_path = os.path.join(tmp_dir, 'signed_document.zip')

# Create a dummy digital signature file
with open(signature_file_path, 'w') as signature_file:
    signature_file.write('This is a dummy digital signature.')

# Create a ZIP file and add the digital signature file
with ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(signature_file_path, arcname='digital_signature.txt')

print(f'ZIP file with digital signature created at: {zip_file_path}')
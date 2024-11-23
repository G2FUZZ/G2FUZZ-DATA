import os
import zipfile
from cryptography.fernet import Fernet

# Create a temporary directory to hold files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Path for the files
signature_file_path = os.path.join(tmp_dir, 'digital_signature.txt')
encrypted_comment_file_path = os.path.join(tmp_dir, 'encrypted_comment.txt')
zip_file_path = os.path.join(tmp_dir, 'signed_document_with_encrypted_comment.zip')

# Create a dummy digital signature file
with open(signature_file_path, 'w') as signature_file:
    signature_file.write('This is a dummy digital signature.')

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a comment
comment = "This is a secret comment."
encrypted_comment = cipher_suite.encrypt(comment.encode())
with open(encrypted_comment_file_path, 'wb') as encrypted_comment_file:
    encrypted_comment_file.write(encrypted_comment)

# Create a ZIP file, add the digital signature file and encrypted comment as a file
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(signature_file_path, arcname='digital_signature.txt')
    zipf.write(encrypted_comment_file_path, arcname='encrypted_comment.txt')
    # Optionally, set the zip file comment (not encrypted in this case)
    # zipf.comment = encrypted_comment  # This would be how to add a comment, but it's not encrypted in the ZIP metadata

print(f'ZIP file with digital signature and encrypted comment created at: {zip_file_path}')
# Note: The encrypted comment is stored as a file inside the zip. Zip file comments cannot be encrypted using the zipfile standard library.
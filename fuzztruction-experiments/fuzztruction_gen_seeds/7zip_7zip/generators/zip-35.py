import os
import zipfile
from cryptography.fernet import Fernet

# Create a temporary directory to hold files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Path for the files
signature_file_path = os.path.join(tmp_dir, 'digital_signature.txt')
encrypted_comment_file_path = os.path.join(tmp_dir, 'encrypted_comment.txt')
embedded_zip_file_path = os.path.join(tmp_dir, 'embedded.zip')
zip_file_path = os.path.join(tmp_dir, 'signed_document_with_encrypted_comment_and_embedded_zip.zip')

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

# Create an embedded ZIP file with a dummy file inside
with zipfile.ZipFile(embedded_zip_file_path, 'w') as embedded_zip:
    embedded_zip.writestr('dummy.txt', 'This is a dummy file inside the embedded zip.')

# Create a ZIP file, add the digital signature file, encrypted comment, and the embedded ZIP as files
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(signature_file_path, arcname='digital_signature.txt')
    zipf.write(encrypted_comment_file_path, arcname='encrypted_comment.txt')
    zipf.write(embedded_zip_file_path, arcname='embedded.zip')
    # Optionally, set the zip file comment
    # zipf.comment = b'This is a zip file comment'  # Example of how to add a non-encrypted comment

print(f'ZIP file with digital signature, encrypted comment, and embedded zip created at: {zip_file_path}')
# Note: The encrypted comment is stored as a file inside the zip. The embedded ZIP is also included as part of the contents.
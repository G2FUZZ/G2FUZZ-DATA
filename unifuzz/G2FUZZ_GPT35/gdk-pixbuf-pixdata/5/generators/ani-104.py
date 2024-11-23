import os
import hashlib
import json

# Define the content of the 'ani' file with extended features
ani_content = """
Resolution Independence: Yes
Allow Various Screen Sizes: Yes
Quality Loss: None
Encryption: AES-256
Metadata:
{
    "author": "John Doe",
    "created_at": "2022-01-15",
    "version": "1.0"
}
"""

# Create a directory to save the 'ani' files if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the generated 'ani' file with the extended content
file_path = './tmp/ani_file_extended.ani'
with open(file_path, 'w') as f:
    f.write(ani_content)

# Calculate and save the hash of the file content
hash_object = hashlib.sha256(ani_content.encode())
hash_digest = hash_object.hexdigest()
hash_file_path = './tmp/ani_file_extended_hash.txt'
with open(hash_file_path, 'w') as hash_file:
    hash_file.write(hash_digest)

print(f"Generated 'ani' file with extended features saved at: {file_path}")
print(f"Hash of the 'ani' file content saved at: {hash_file_path}")
import os
import zlib
import base64

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' file with encryption and compression
file_content = "Complex File Features: This 'ani' file includes encryption and compression for enhanced security and reduced file size."

# Encryption function
def encrypt_data(data):
    # Perform encryption logic here
    encrypted_data = data.encode('utf-8')  # Placeholder encryption
    return encrypted_data

# Compression function
def compress_data(data):
    compressed_data = zlib.compress(data)
    return compressed_data

# Save the generated file with encryption and compression
file_path = './tmp/ani_file_extended.ani'
with open(file_path, 'wb') as file:
    encrypted_content = encrypt_data(file_content)
    compressed_content = compress_data(encrypted_content)
    encoded_content = base64.b64encode(compressed_content)
    file.write(encoded_content)

print(f"Extended File saved at: {file_path}")
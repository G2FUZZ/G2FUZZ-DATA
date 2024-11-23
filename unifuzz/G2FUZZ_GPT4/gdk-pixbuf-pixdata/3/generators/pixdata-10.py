import os
from cryptography.fernet import Fernet

# Directory where the pixdata files will be saved
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sample data to be encrypted, representing "pixdata"
sample_data = {
    "feature": "Encryption and Security Features",
    "description": "Offers options for encrypting the file or parts of its content to protect sensitive information or copyrighted material."
}

# Convert the sample data into bytes
data_bytes = str(sample_data).encode()

# Encrypt the data
encrypted_data = cipher_suite.encrypt(data_bytes)

# Path where the encrypted file will be saved
file_path = os.path.join(output_dir, "encrypted_pixdata")

# Write the encrypted data to a file
with open(file_path, "wb") as file:
    file.write(encrypted_data)

# Save the key to a separate file for decryption purposes
key_path = os.path.join(output_dir, "encryption_key")
with open(key_path, "wb") as key_file:
    key_file.write(key)

print(f"Encrypted pixdata file saved to {file_path}")
print(f"Encryption key saved to {key_path}")
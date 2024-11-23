from cryptography.fernet import Fernet
import os

def generate_encrypted_file(file_path, data):
    # Generate a key for encryption
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(data.encode())
    
    # Ensure the ./tmp/ directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the encrypted data to a file
    with open(file_path, 'wb') as file_out:
        file_out.write(encrypted_data)
    
    # Optionally, save the key to a separate file for decryption purposes
    key_file_path = os.path.join(os.path.dirname(file_path), 'encryption_key.key')
    with open(key_file_path, 'wb') as key_out:
        key_out.write(key)

    print(f"Encrypted file saved to {file_path}")
    print(f"Encryption key saved to {key_file_path}")

# Sample data to encrypt
sample_data = "This is an example of encrypted content for DRM purposes."

# Specify the path to the encrypted file
encrypted_file_path = './tmp/encrypted_pixdata.file'

# Generate and save the encrypted file
generate_encrypted_file(encrypted_file_path, sample_data)
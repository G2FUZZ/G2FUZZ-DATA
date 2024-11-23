import numpy as np
import cv2
import os
from cryptography.fernet import Fernet
from PIL import Image

def encrypt_file(file_path, key):
    """
    Encrypts a file using the provided key.
    """
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
    """
    Decrypts a file using the provided key.
    """
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an example image, using a 256x256 pixels image with 3 channels (RGB)
# The image will display gradients in all three channels
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient for each channel
for i in range(256):
    image[i, :, 0] = i  # Red channel gradient
    image[:, i, 1] = i  # Green channel gradient
    image[i, :, 2] = 255-i  # Blue channel, inverse gradient

# Define the TIFF file path with JPEG compression
tiff_file_path = os.path.join(output_dir, 'lossy_compressed_image.tiff')

# Save the image with JPEG compression (lossy) inside a TIFF
image_pil = Image.fromarray(image)
image_pil.save(tiff_file_path, compression="jpeg", quality=90)  # Adjust quality for more or less compression

# Generate a key for encryption
key = Fernet.generate_key()

# Encrypt the TIFF file
encrypt_file(tiff_file_path, key)

print(f"Image saved and encrypted as {tiff_file_path}")
print(f"Encryption key (keep this secure): {key.decode()}")

# To decrypt the file, use the `decrypt_file` function with the same key.
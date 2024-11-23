from PIL import Image
import numpy as np
import os
from cryptography.fernet import Fernet

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Create an image with a gradient
width, height = 800, 600
image = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        # Gradient from black to white
        value = int((x / width) * 255)
        image.putpixel((x, y), (value, value, value))

# Save the image with JPEG compression
image_path = './tmp/gradient_image.jpg'
image.save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

# Read the saved image file for encryption
with open(image_path, 'rb') as file:
    original_image_data = file.read()

# Encrypt the image data
encrypted_image_data = cipher_suite.encrypt(original_image_data)

# Save the encrypted image data to a new file
encrypted_image_path = './tmp/gradient_image_encrypted.jpg'
with open(encrypted_image_path, 'wb') as file:
    file.write(encrypted_image_data)

print(f"Image saved with standard compression to {image_path}")
print(f"Encrypted image saved to {encrypted_image_path}")
print(f"Encryption key (keep this secure to decrypt the image): {key}")

# Note: To view the encrypted image, you will need to decrypt it using the provided key.
# Below is an example code snippet for decrypting the image (you would run this where you want to decrypt and view the image):

# Example decryption code (to be used where decryption is necessary):
# cipher_suite = Fernet(key)  # Initialize the cipher suite with the same key used for encryption
# with open(encrypted_image_path, 'rb') as file:
#     encrypted_data = file.read()
# decrypted_data = cipher_suite.decrypt(encrypted_data)
# with open('./tmp/gradient_image_decrypted.jpg', 'wb') as file:
#     file.write(decrypted_data)
# decrypted_image = Image.open('./tmp/gradient_image_decrypted.jpg')
# decrypted_image.show()

# This extended code demonstrates adding a "Security Features" feature by encrypting the JPEG file,
# which can be considered a form of DRM to control distribution and access.
from PIL import Image, ImageDraw
import os
from cryptography.fernet import Fernet

# Function to generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the current directory named `secret.key`
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt the image data
def encrypt_image_data(image_data):
    key = load_key()
    f = Fernet(key)
    encrypted_image_data = f.encrypt(image_data)
    return encrypted_image_data

# Create a new image with RGB channels
width, height = 800, 600
image = Image.new('RGB', (width, height))

# Create a gradient
draw = ImageDraw.Draw(image)
for i in range(width):
    for j in range(height):
        red = int((i/width) * 255)
        green = int((j/height) * 255)
        blue = 255 - red
        draw.point((i, j), fill=(red, green, blue))

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a new key for encryption
write_key()

# Save the image temporarily to read its byte data
temp_image_path = './tmp/temp_image.jpg'
image.save(temp_image_path, 'JPEG', quality=85)

# Read the image data
with open(temp_image_path, 'rb') as image_file:
    image_data = image_file.read()

# Encrypt the image data
encrypted_image_data = encrypt_image_data(image_data)

# Save the encrypted image data to a new file
encrypted_image_path = './tmp/encrypted_chroma_subsampling_example.jpg'
with open(encrypted_image_path, 'wb') as encrypted_image_file:
    encrypted_image_file.write(encrypted_image_data)

# Optionally, delete the temporary image file
os.remove(temp_image_path)

print(f'Encrypted image saved to {encrypted_image_path}')
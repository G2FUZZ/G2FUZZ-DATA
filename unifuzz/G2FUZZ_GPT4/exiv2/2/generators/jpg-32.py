from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import cv2
from cryptography.fernet import Fernet
import json
from io import BytesIO

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

# Add watermark to the image using opencv-python
cv_image = np.array(image)
cv_watermark_text = "Sample Watermark"
cv_font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(cv_image, cv_watermark_text, (10, height - 10), cv_font, 1, (255, 255, 255), 2, cv2.LINE_AA, False)
image_with_watermark = Image.fromarray(cv_image)

# Embed metadata into the image
metadata = {"Author": "John Doe", "Description": "Sample Gradient Image with Watermark"}
metadata_bytes = bytes(json.dumps(metadata), 'utf-8')
# Create a new image with an additional channel for metadata (alpha channel)
image_with_metadata = Image.new("RGBA", image_with_watermark.size)
image_with_metadata.paste(image_with_watermark)
# Use the alpha channel to store metadata text
draw = ImageDraw.Draw(image_with_metadata)
font = ImageFont.load_default()
draw.text((10, 10), json.dumps(metadata), fill=(255, 255, 255, 128), font=font)

# Save the image with JPEG compression
image_path = './tmp/gradient_image_with_metadata_and_watermark.jpg'
image_with_metadata.convert('RGB').save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

# Read the saved image file for encryption
with open(image_path, 'rb') as file:
    original_image_data = file.read()

# Encrypt the image data
encrypted_image_data = cipher_suite.encrypt(original_image_data)

# Save the encrypted image data to a new file
encrypted_image_path = './tmp/gradient_image_encrypted.jpg'
with open(encrypted_image_path, 'wb') as file:
    file.write(encrypted_image_data)

print(f"Image with metadata and watermark saved with standard compression to {image_path}")
print(f"Encrypted image saved to {encrypted_image_path}")
print(f"Encryption key (keep this secure to decrypt the image): {key}")

# Example decryption code (to be used where decryption is necessary):
# cipher_suite = Fernet(key)  # Initialize the cipher suite with the same key used for encryption
# with open(encrypted_image_path, 'rb') as file:
#     encrypted_data = file.read()
# decrypted_data = cipher_suite.decrypt(encrypted_data)
# with open('./tmp/gradient_image_decrypted.jpg', 'wb') as file:
#     file.write(decrypted_data)
# decrypted_image = Image.open('./tmp/gradient_image_decrypted.jpg')
# decrypted_image.show()

# Note: The metadata is embedded visually in the image and not in the file's metadata section.
# For embedding metadata directly into the JPEG's EXIF or XMP tags, consider using specialized libraries like `Pillow` for basic EXIF data or `piexif` for more advanced manipulations.
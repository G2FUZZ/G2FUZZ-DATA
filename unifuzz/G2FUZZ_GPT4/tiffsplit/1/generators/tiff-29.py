from PIL import Image
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a digital signature for data
def generate_digital_signature(data, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Function to save image and its digital signature
def save_image_with_signature(image, path, compression, signature):
    # Save the image with specified compression
    image_path = os.path.join('./tmp/', path)
    if compression == "tiff_deflate":
        # Note: 'compression' argument's value should be directly supported by PIL, adjust as necessary
        image.save(image_path, format='TIFF', compression='tiff_deflate')
    else:
        image.save(image_path)

    # Save the digital signature in a separate file
    signature_path = os.path.join('./tmp/', path + ".signature")
    with open(signature_path, "w") as sig_file:
        signature_str = signature.hex()
        sig_file.write(signature_str)

# Generate an RGB image with Deflate Compression
rgb_image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square

# Dummy data to sign
data_to_sign = b"Image data that needs to be signed"

# Path to private key
private_key_path = "./tmp/private_key.pem"

# Generate a digital signature for the data
signature = generate_digital_signature(data_to_sign, private_key_path)

# Save the image with a digital signature
save_image_with_signature(rgb_image, 'rgb_image_with_signature.tiff', "tiff_deflate", signature)
from PIL import Image
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives import serialization
from PIL import TiffImagePlugin
from PIL import TiffTags

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_and_save_private_key(private_key_path):
    # Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Serialize private key to PEM format
    pem = private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=NoEncryption()
    )

    # Write the PEM format private key to file
    with open(private_key_path, "wb") as key_file:
        key_file.write(pem)

# Function to generate a digital signature for data
def generate_digital_signature(data, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = load_pem_private_key(
            key_file.read(),
            password=None,
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

# Function to save image with additional complex features
def save_complex_image_with_signature(images, path, compression, signature, dpi=(300, 300), metadata=None):
    # Initialize TIFF save parameters
    save_kwargs = {
        "format": "TIFF",
        "save_all": True,  # For multi-page
        "compression": compression,
        "dpi": dpi
    }

    # Adjust metadata if provided
    if metadata is not None:
        # PIL expects TIFFTAG keys to be integers. Example: {270: 'Description'}
        tiffinfo = TiffImagePlugin.ImageFileDirectory_v2()
        for tag, value in metadata.items():
            tag_id = TiffTags.TAGS_V2.get(tag, None)
            if tag_id:
                tiffinfo[tag_id] = value
        save_kwargs["tiffinfo"] = tiffinfo

    # Process and save the first image to start the multi-page TIFF
    image_path = os.path.join('./tmp/', path)
    images[0].save(image_path, **save_kwargs)

    # Append additional images to the TIFF
    for image in images[1:]:
        save_kwargs['append_images'] = [image]
        image.save(image_path, **save_kwargs)

    # Save the digital signature in a separate file
    signature_path = os.path.join('./tmp/', path + ".signature")
    with open(signature_path, "wb") as sig_file:
        sig_file.write(signature)

# Path to private key
private_key_path = "./tmp/private_key.pem"

# Ensure the private key exists before generating a digital signature
generate_and_save_private_key(private_key_path)

# Dummy data to sign
data_to_sign = b"Image data that needs to be signed"

# Generate a digital signature for the data
signature = generate_digital_signature(data_to_sign, private_key_path)

# Generate multiple RGB images for a multi-page TIFF
images = [
    Image.new("RGB", (100, 100), (255, 0, 0)),  # Red square
    Image.new("RGB", (100, 100), (0, 255, 0)),  # Green square
    Image.new("RGB", (100, 100), (0, 0, 255))   # Blue square
]

# Custom metadata
metadata = {
    "Artist": "John Doe",
    "Description": "This is a multi-page TIFF with custom DPI and metadata."
}

# Save the images with a digital signature
save_complex_image_with_signature(images, 'complex_image_with_signature.tiff', "tiff_deflate", signature, dpi=(300, 300), metadata=metadata)
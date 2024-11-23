import os
from PIL import Image, JpegImagePlugin
from stegano import lsb

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a base image (full-size)
base_image = Image.new('RGB', (800, 600), 'blue')

# Create a thumbnail (smaller version)
thumbnail_size = (80, 60)
thumbnail_image = base_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image's info dictionary
base_image.info['thumbnail'] = thumbnail_image

# Now, adding Security Features - embedding a hidden message using steganography
secret_message = "This is a hidden message for copyright protection."
base_image_with_secret = lsb.hide(base_image, secret_message)

# Save the image with the embedded thumbnail, hidden message, and restart markers
output_path = os.path.join(output_dir, 'image_with_security_features.jpg')

# Save options, excluding the hypothetical 'restart' option, as it's not supported
save_options = {
    "quality": 95,
    "optimize": True,
    "progressive": True,
    "dpi": (72, 72),
    "icc_profile": base_image.info.get('icc_profile',''),
    "subsampling": "4:2:0"
}

# Saving the image with security features
base_image_with_secret.save(output_path, 'JPEG', **save_options)

print(f"Image saved with an embedded thumbnail and hidden message at: {output_path}")
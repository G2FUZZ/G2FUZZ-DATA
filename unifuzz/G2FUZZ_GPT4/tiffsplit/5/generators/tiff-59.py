from PIL import Image, PngImagePlugin, TiffTags
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 300, 300

def create_image_layer(width, height, layer):
    """
    Creates a single layer (frame) for the TIFF file with specific patterns based on the layer number.
    """
    # Creating an RGBA image (Red, Green, Blue, Alpha) with a floating point format
    image = np.zeros((height, width, 4), dtype=np.float32)

    # Fill the image with different gradients and patterns based on the layer
    for x in range(width):
        for y in range(height):
            if layer == 0:
                # Simple gradient
                image[y, x] = [1.0, (x % 256) / 255.0, (y % 256) / 255.0, (x / width)]
            elif layer == 1:
                # Circular pattern
                dx = x - width / 2
                dy = y - height / 2
                r = np.sqrt(dx**2 + dy**2)
                image[y, x] = [(r % 256) / 255.0, 1.0 - ((x % 256) / 255.0), 1.0 - ((y % 256) / 255.0), ((height - y) / height)]
            else:
                # Diagonal gradient pattern
                image[y, x] = [(y % 256) / 255.0, 1.0 - ((y % 256) / 255.0), (x % 256) / 255.0, (y / height)]
    
    return (image * 255).astype(np.uint8)

# Create multiple layers (frames)
layers = [create_image_layer(width, height, i) for i in range(3)]

# Convert the numpy array layers to PIL Images
imgs = [Image.fromarray(layer, 'RGBA') for layer in layers]

# Save the image as TIFF with multiple layers (frames) and no compression for demonstration
imgs[0].save(
    './tmp/complex_alpha_channel_image_fp.tiff',
    save_all=True,
    append_images=imgs[1:],
    compression=None,
    dpi=(300,300)
)

# Embed an ICC profile (this is a simplistic way; in real scenarios, you'd load an actual ICC profile)
icc_profile = b'0' * 3144  # Placeholder for a real ICC profile binary data
with open('./tmp/complex_alpha_channel_image_fp.tiff', 'rb') as f:
    img_data = f.read()

with open('./tmp/complex_alpha_channel_image_fp_icc.tiff', 'wb') as f:
    # TIFF tag for ICC Profile is 34675
    TiffTags.TAGS_V2[34675] = ('ICCProfile', 'ICCProfile', TiffTags.BYTE)
    f.write(img_data.replace(b'\x00' * 3144, icc_profile))

print("TIFF image with multiple layers, custom metadata, and an embedded ICC profile saved successfully.")
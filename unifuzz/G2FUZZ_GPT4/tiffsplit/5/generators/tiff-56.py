from PIL import Image, ImageSequence
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 300, 300

def create_frame(x_shift):
    """Function to create a single frame with a specific gradient."""
    # Creating an RGBA image (Red, Green, Blue, Alpha)
    image = np.zeros((height, width, 4), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            # Modifying the gradient with x_shift for frame variation
            image[y, x] = [255, (x + x_shift) % 256, y % 256, int(255 * ((x + x_shift) / width))]
    return Image.fromarray(image, 'RGBA')

# Create multiple frames for the TIFF
frames = [create_frame(x_shift) for x_shift in range(0, 100, 20)]

# Save the multi-frame TIFF
# Defining a custom tag - e.g., ImageDescription
custom_tags = {
    270: ("A multi-frame TIFF with gradients and custom tags.",),
}
# Use the save_all parameter to indicate a multi-frame save and apply compression
frames[0].save(
    './tmp/multi_frame_alpha_channel_image.tiff',
    save_all=True,
    append_images=frames[1:],
    compression='tiff_deflate',  # Using deflate compression
    tiffinfo=custom_tags
)

print("Multi-frame TIFF image with alpha channel, custom tags, and compression saved successfully.")
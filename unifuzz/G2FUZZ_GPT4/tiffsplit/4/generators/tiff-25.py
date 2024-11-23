from PIL import Image, ImageChops
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_stereoscopic_image(base_image):
    """
    Generates a stereoscopic pair by simulating a slight horizontal shift
    between two images.
    """
    # Create a slightly shifted version of the image for the stereoscopic effect
    offset = base_image.width // 50  # Slight horizontal shift
    left_image = ImageChops.offset(base_image, offset, 0)
    right_image = ImageChops.offset(base_image, -offset, 0)

    # Combine the shifted images into one (side by side)
    total_width = base_image.width * 2
    stereoscopic_image = Image.new('RGB', (total_width, base_image.height))
    stereoscopic_image.paste(left_image, (0, 0))
    stereoscopic_image.paste(right_image, (base_image.width, 0))

    return stereoscopic_image

# Create a new image with RGB mode
width, height = 800, 600
base_image = Image.new("RGB", (width, height), "white")

# Generate a stereoscopic image
stereoscopic_image = generate_stereoscopic_image(base_image)

# Save the stereoscopic image as a TIFF with tiles
tile_width, tile_height = 256, 256
stereoscopic_image.save('./tmp/stereoscopic_tiled_image.tiff', format='TIFF', tile=('raw', (tile_width, tile_height)))

print("Stereoscopic TIFF image with tiles saved successfully.")
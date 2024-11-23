from PIL import Image, ImageDraw
import numpy as np
import os

def create_image(width, height, pattern, text=None, color_space="RGBA"):
    """
    Create an image with a specified pattern and optional text.
    """
    if color_space == "L":  # Grayscale
        image = np.zeros((height, width), dtype=np.uint8) + 255  # Fill with white for grayscale
    else:  # Assume RGBA for all other cases
        image = np.zeros((height, width, 4), dtype=np.uint8)
        image.fill(255)  # Fill with white background for RGBA

    pil_img = Image.fromarray(image, color_space)
    draw = ImageDraw.Draw(pil_img)

    if pattern == 'gradient':
        for x in range(width):
            for y in range(height):
                if color_space == "L":
                    pil_img.putpixel((x, y), int(255 * (x / width)))
                else:
                    pil_img.putpixel((x, y), (255, x % 256, y % 256, int(255 * (x / width))))
    elif pattern == 'circles':
        for x in range(50, width, 100):
            for y in range(50, height, 100):
                radius = int((x % 100 + y % 100) / 4)
                if color_space == "L":
                    # Use a grayscale value for fill when in grayscale mode
                    gray_value = int((x + y) % 256)  # Example grayscale value based on x and y
                    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=gray_value)
                else:
                    # Use an RGBA tuple for fill when in RGBA mode
                    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(x % 256, y % 256, 255, 255))
    elif pattern == 'lines':
        for x in range(0, width, 10):
            draw.line((x, 0, width-x, height), fill=(255, x % 256, 0, 255))

    if text:
        draw.text((10, 10), text, fill="black" if color_space == "RGBA" else 255)

    image = np.array(pil_img)
    return image

def save_tiff(images, file_path, dpi_settings, custom_tags):
    """
    Save multiple images to a single TIFF file with varying resolutions and custom metadata.
    """
    imgs = [Image.fromarray(img) for img in images]
    imgs[0].save(
        file_path,
        save_all=True,
        append_images=imgs[1:],
        compression="tiff_lzw",
        dpi=dpi_settings[0],
        tiffinfo={**custom_tags[0]}
    )
    # Note: PIL does not support varying dpi or tiffinfo directly through save parameters for append_images

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size, patterns, and additional properties
patterns = [('gradient', None, "RGBA"), ('circles', "Circle Pattern", "L"), ('lines', "Line Art", "RGBA")]
width, height = 300, 300
dpi_settings = [(300.0, 300.0), (150.0, 150.0), (600.0, 300.0)]
custom_tags = [
    {270: "Gradient Pattern"},  # ImageDescription for the first image
    {270: "Circles in Grayscale"},  # for the second
    {270: "Lines with transparency"}  # for the third
]

# Create images with different patterns
images = [create_image(width, height, pattern[0], text=pattern[1], color_space=pattern[2]) for pattern in patterns]

# Save the images as pages in a single TIFF file with custom dpi and metadata
save_tiff(images, './tmp/complex_structure_image.tiff', dpi_settings, custom_tags)

print("TIFF image with complex structures saved successfully.")
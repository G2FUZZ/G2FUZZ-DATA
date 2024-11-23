from PIL import Image, ImageDraw
import os

def create_spot_color_image(width, height, spot_rectangle, spot_color, background_color=(0, 0, 0, 0)):
    """
    Creates an image with a spot color area.

    Parameters:
    - width: Width of the image.
    - height: Height of the image.
    - spot_rectangle: A tuple defining the (left, top, right, bottom) of the rectangle.
    - spot_color: The CMYK color for the spot area.
    - background_color: The background CMYK color of the image.

    Returns:
    - An Image object with the specified design.
    """
    # Create a new image with CMYK color mode
    image = Image.new("CMYK", (width, height), background_color)

    # Simulate a spot color by filling part of the image
    draw = ImageDraw.Draw(image)
    draw.rectangle(spot_rectangle, fill=spot_color)

    return image

def save_multi_frame_tiff(images, path):
    """
    Saves multiple images into a single multi-frame TIFF file.

    Parameters:
    - images: A list of Image objects to be saved in the TIFF.
    - path: Path where the TIFF file will be saved.
    """
    # Ensure the first image is saved with save_all=True and append_images contains the rest
    images[0].save(path, save_all=True, append_images=images[1:])

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define parameters for the images
width, height = 100, 100
spot_colors = [(0, 255, 255, 0), (255, 0, 255, 0), (255, 255, 0, 0)]  # Different spot colors
background_color = (0, 0, 0, 0)  # Pure black in CMYK

# Create several images with different spot colors
images = []
for i, color in enumerate(spot_colors):
    spot_rectangle = (25, 25, 75, 75)  # Same spot position for simplicity
    image = create_spot_color_image(width, height, spot_rectangle, color, background_color)
    images.append(image)

# Save the images as a multi-frame TIFF
save_multi_frame_tiff(images, './tmp/multi_frame_spot_color_simulation.tiff')
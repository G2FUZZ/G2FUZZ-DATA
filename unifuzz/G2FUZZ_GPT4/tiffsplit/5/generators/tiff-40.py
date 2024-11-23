from PIL import Image, ImageDraw
import numpy as np
import os

def create_image(width, height, pattern):
    """
    Create an image with a specified pattern.
    """
    image = np.zeros((height, width, 4), dtype=np.uint8)
    if pattern == 'gradient':
        for x in range(width):
            for y in range(height):
                image[y, x] = [255, x % 256, y % 256, int(255 * (x / width))]
    elif pattern == 'circles':
        image.fill(255)  # Fill with white background
        pil_img = Image.fromarray(image, 'RGBA')
        draw = ImageDraw.Draw(pil_img)
        for x in range(50, width, 100):
            for y in range(50, height, 100):
                radius = int((x % 100 + y % 100) / 4)
                draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(x % 256, y % 256, 255, 255))
        image = np.array(pil_img)
    elif pattern == 'lines':
        image.fill(255)  # Fill with white background
        pil_img = Image.fromarray(image, 'RGBA')
        draw = ImageDraw.Draw(pil_img)
        for x in range(0, width, 10):
            draw.line((x, 0, width-x, height), fill=(255, x % 256, 0, 255))
        image = np.array(pil_img)
    return image

def save_tiff(images, file_path):
    """
    Save multiple images to a single TIFF file.
    """
    imgs = [Image.fromarray(img, 'RGBA') for img in images]
    imgs[0].save(file_path, save_all=True, append_images=imgs[1:])

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size and patterns
patterns = ['gradient', 'circles', 'lines']
width, height = 300, 300

# Create images with different patterns
images = [create_image(width, height, pattern) for pattern in patterns]

# Save the images as pages in a single TIFF file
save_tiff(images, './tmp/complex_structure_image.tiff')

print("TIFF image with complex structures saved successfully.")
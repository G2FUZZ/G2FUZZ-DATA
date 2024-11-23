from PIL import Image, ImageDraw
import numpy as np
import os

def create_image(width, height, pattern):
    """
    Create an image with a specified pattern.
    """
    if pattern in ['red', 'green', 'blue']:  # For simple color patterns
        image = Image.new("RGB", (width, height), pattern)
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), "Sample", fill="black")
    else:  # For complex patterns
        image = np.zeros((height, width, 3), dtype=np.uint8)  # Use RGB for simplicity
        if pattern == 'gradient':
            for x in range(width):
                for y in range(height):
                    image[y, x] = [x % 256, y % 256, (x+y) % 256]
            image = Image.fromarray(image, 'RGB')
        elif pattern == 'circles':
            image.fill(255)  # Fill with white background
            pil_img = Image.fromarray(image, 'RGB')
            draw = ImageDraw.Draw(pil_img)
            for x in range(50, width, 100):
                for y in range(50, height, 100):
                    radius = int((x % 100 + y % 100) / 4)
                    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(x % 256, y % 256, 255))
            image = pil_img
        elif pattern == 'lines':
            image.fill(255)  # Fill with white background
            pil_img = Image.fromarray(image, 'RGB')
            draw = ImageDraw.Draw(pil_img)
            for x in range(0, width, 10):
                draw.line((x, 0, width-x, height), fill=(255, x % 256, 0))
            image = pil_img
    return image

def save_tiff(images, file_path):
    """
    Save multiple images to a single TIFF file with LZW compression and Predictor Tag.
    """
    imgs = [img for img in images]
    imgs[0].save(
        file_path, 
        save_all=True, 
        compression="tiff_lzw", 
        append_images=imgs[1:],
        tiffinfo={317: 2}  # 317 is the tag number for Predictor
    )

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Patterns and image size
patterns = ['red', 'green', 'blue', 'gradient', 'circles', 'lines']
width, height = 100, 100

# Create images with different patterns
images = [create_image(width, height, pattern) for pattern in patterns]

# Save the images as pages in a single TIFF file with LZW compression and Predictor Tag
tiff_path = os.path.join(output_dir, 'multi_pattern_image_with_predictor.tiff')
save_tiff(images, tiff_path)

print("TIFF image with multiple patterns and compression settings saved successfully.")
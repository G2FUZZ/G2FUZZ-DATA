from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image for demonstration purposes
def create_image(width, height, color):
    image = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Sample", fill="black")
    return image

# Create multiple images
image1 = create_image(100, 100, "red")
image2 = create_image(100, 100, "green")
image3 = create_image(100, 100, "blue")

# Save images as a multi-page TIFF
tiff_path = os.path.join(output_dir, 'multi_image.tiff')
image1.save(tiff_path, save_all=True, append_images=[image2, image3])
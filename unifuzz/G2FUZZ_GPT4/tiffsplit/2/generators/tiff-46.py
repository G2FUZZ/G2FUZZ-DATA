from PIL import Image, ImageDraw, ImageFont, ExifTags
import datetime
import os

def create_color_gradient(width, height):
    """Generate a simple horizontal color gradient from blue to green."""
    base_image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(base_image)
    for i in range(width):
        r = int(255 * (i / width))
        g = 255 - int(255 * (i / width))
        b = 125  # Constant to add a touch of blue across the gradient
        draw.line([(i, 0), (i, height)], fill=(r, g, b))
    return base_image

# Ensure the directory exists
save_directory = "./tmp/"
os.makedirs(save_directory, exist_ok=True)

# Simplified function to demonstrate saving a file
def save_sample_image():
    width, height = 100, 100
    image = create_color_gradient(width, height)
    save_path = f"{save_directory}sample_image.tiff"
    image.save(save_path, "TIFF")

save_sample_image()
print("Sample TIFF image with a color gradient has been generated and saved.")
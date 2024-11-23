from PIL import Image, ImageDraw

# Function to create a simple image with a specified color
def create_image_with_color(color, size=(100, 100)):
    image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    # Adding some text to differentiate between the layers
    draw.text((10, 40), f"Layer {color}", fill="white")
    return image

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
images = [create_image_with_color(color) for color in colors]  # Corrected function name here

# Ensure the ./tmp/ directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the images as a multi-page TIFF
images[0].save('./tmp/multi_page.tiff', save_all=True, append_images=images[1:])

print("Multi-page TIFF has been saved in ./tmp/multi_page.tiff")
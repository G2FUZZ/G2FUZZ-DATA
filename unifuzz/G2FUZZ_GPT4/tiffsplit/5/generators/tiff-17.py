from PIL import Image, ImageDraw
import os

# Function to create a simple image with a specified color
def create_image_with_color(color, size=(100, 100), color_map=None):
    if color_map is not None:
        # Create an indexed image if a color map is provided
        image = Image.new("P", size)
        image.putpalette(color_map)
        image.paste(0, [0, 0, image.size[0], image.size[1]])  # Fill with the first color in the palette
    else:
        # Create a regular RGB image
        image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    # Adding some text to differentiate between the layers
    draw.text((10, 40), f"Layer {color}", fill="white")
    return image

def generate_color_map():
    # Create a simple color map with 256 colors
    # This example just cycles through red, green, and blue
    color_map = []
    for i in range(256):
        if i < 85:
            color_map.extend([i * 3, 0, 0])  # Red
        elif i < 170:
            color_map.extend([0, (i-85) * 3, 0])  # Green
        else:
            color_map.extend([0, 0, (i-170) * 3])  # Blue
    return color_map

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
color_map = generate_color_map()
# Corrected the function call to use create_image_with_color
images = [create_image_with_color(color, color_map=color_map) for color in colors]

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the first image to initiate the multi-page TIFF with color map
images[0].save('./tmp/multi_page_with_color_map.tiff', save_all=True, append_images=images[1:], color_mode="P")

print("Multi-page TIFF with Color Map Storage has been saved in ./tmp/multi_page_with_color_map.tiff")
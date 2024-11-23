from PIL import Image, ImageDraw
import os

# Function to create a simple image with a specified color
def create_image_with_color(color, size=(100, 100)):
    image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    # Adding some text to differentiate between the layers
    draw.text((10, 40), f"Layer {color}", fill="white")
    return image

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
images = [create_image_with_color(color) for color in colors]

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the first image to initiate the multi-page TIFF
images[0].save('./tmp/multi_page_with_custom_tags.tiff')

# Now, append the rest of the images
for img in images[1:]:
    img.save('./tmp/multi_page_with_custom_tags.tiff', save_all=True, append_images=[img])

print("Multi-page TIFF without custom tags has been saved in ./tmp/multi_page_with_custom_tags.tiff")
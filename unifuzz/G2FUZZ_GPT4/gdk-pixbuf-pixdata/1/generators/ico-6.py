import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_icon_file(filename, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Create an ICO file with multiple resolutions for scalability.
    
    Args:
    - filename: The name of the ICO file to save.
    - sizes: A list of tuple sizes for the ICO file.
    """
    # Create a list to hold the images for each size
    icon_images = []
    
    for size in sizes:
        # Create a new image with RGBA mode
        image = Image.new('RGBA', size, (255, 255, 255, 0))
        
        # Draw a simple shape to visualize the icon
        draw = ImageDraw.Draw(image)
        draw.ellipse((0, 0, size[0], size[1]), fill=(255, 165, 0, 255), outline=(0, 0, 0, 255))
        
        # Append the resized image to the list
        icon_images.append(image)
    
    # Save the images as an ICO file
    icon_images[0].save(filename, format='ICO', sizes=[img.size for img in icon_images])

# Generate the ICO file with multiple resolutions
create_icon_file('./tmp/scalable_icon.ico')
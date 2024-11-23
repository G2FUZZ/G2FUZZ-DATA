from PIL import Image, ImageDraw

def create_gradient(width, height, color1, color2):
    """
    Creates an image with a horizontal gradient between two colors.
    
    :param width: Width of the image
    :param height: Height of the image
    :param color1: The starting color of the gradient (left)
    :param color2: The ending color of the gradient (right)
    :return: An image with a horizontal gradient
    """
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (x / width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Create a gradient image
width, height = 800, 600
color1 = (255, 0, 0)  # Red
color2 = (0, 0, 255)  # Blue
image = create_gradient(width, height, color1, color2)

# Make sure the /tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/gradient_png.png')
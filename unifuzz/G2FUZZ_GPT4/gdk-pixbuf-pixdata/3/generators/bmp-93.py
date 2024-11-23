import os
from PIL import Image, ImageDraw, ImageFont

def create_gradient(width, height, start_color, end_color):
    """
    Creates a vertical gradient between two colors.

    Parameters:
    - width: Width of the gradient image.
    - height: Height of the gradient image.
    - start_color: Starting color (top) as a tuple (R, G, B).
    - end_color: Ending color (bottom) as a tuple (R, G, B).

    Returns:
    - An Image object with the gradient.
    """
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def add_text(image, text, position, font_path, font_size, color):
    """
    Adds text to an image.

    Parameters:
    - image: The Image object to draw text on.
    - text: The text to add.
    - position: The position tuple (x, y) where the text will be added.
    - font_path: The path to the .ttf font file or None for default font.
    - font_size: The size of the font.
    - color: The color of the text as a tuple (R, G, B).

    Returns:
    - An Image object with text added.
    """
    draw = ImageDraw.Draw(image)
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        # Use a default font if no font path is provided
        font = ImageFont.load_default()
    draw.text(position, text, fill=color, font=font)
    return image

# Create the directory for output if it does not exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Image size
width, height = 400, 200

# Create a gradient background from blue to light blue
gradient_image = create_gradient(width, height, (0, 0, 255), (173, 216, 230))

# Add text over the gradient
# Note: You'll need to specify a path to a .ttf font file on your system for this to work
# For demonstration, we'll use PIL's default font by passing None, but for custom fonts, replace None with 'path/to/your/font.ttf'
font_path = None  # Example: '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
gradient_with_text = add_text(gradient_image, "Hello, World!", (50, 75), font_path, 40, (255, 255, 255))

# Save the image as BMP
gradient_with_text.save(os.path.join(output_dir, "complex_feature.bmp"), "BMP")

print("BMP image with complex features created and saved as 'complex_feature.bmp' in './tmp/'.")
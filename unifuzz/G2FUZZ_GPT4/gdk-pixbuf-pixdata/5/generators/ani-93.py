from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_frame_image(size, color, text, opacity):
    """Create a single frame image with specified size, color, and text."""
    # Adjust opacity
    color_with_opacity = (color[0], color[1], color[2], opacity)
    
    image = Image.new('RGBA', size, color_with_opacity)
    draw = ImageDraw.Draw(image)
    
    # Optional: Adding text to the frame
    try:
        # Attempt to use a default font
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        # Fallback if the specific font is not found
        font = ImageFont.load_default()
    
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)
    draw.text(text_position, text, fill='white', font=font)
    
    return image
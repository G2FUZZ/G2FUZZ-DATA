import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_complex_icon_file(filename, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Create an ICO file with multiple resolutions for scalability, including complex structures
    like layers, shapes, and text.
    
    Args:
    - filename: The name of the ICO file to save.
    - sizes: A list of tuple sizes for the ICO file.
    """
    # Create a list to hold the images for each size
    icon_images = []
    
    for size in sizes:
        # Create a new image with RGBA mode
        image = Image.new('RGBA', size, (255, 255, 255, 0))
        
        # Draw a complex shape to visualize the icon
        draw = ImageDraw.Draw(image)
        
        # Background rectangle
        draw.rectangle((0, 0, size[0], size[1]), fill=(70, 130, 180, 255), outline=(255, 255, 255, 255))
        
        # Ellipse overlay
        ellipse_size = (size[0] * 0.1, size[1] * 0.1, size[0] * 0.9, size[1] * 0.9)
        draw.ellipse(ellipse_size, fill=(255, 165, 0, 255), outline=(0, 0, 0, 255))
        
        # Adding a simple text overlay
        try:
            # Try to use a common font
            font = ImageFont.truetype("arial.ttf", int(size[0] * 0.2))
        except IOError:
            # Fallback to PIL's default font if specific font is not found
            font = ImageFont.load_default()
        
        text = "ICO"
        textwidth, textheight = draw.textsize(text, font=font)
        texttop = (size[0] - textwidth) / 2
        textleft = (size[1] - textheight) / 2
        draw.text((texttop, textleft), text, font=font, fill=(255, 255, 255, 255))
        
        # Append the resized image to the list
        icon_images.append(image)
    
    # Save the images as an ICO file
    icon_images[0].save(filename, format='ICO', sizes=[img.size for img in icon_images])

# Generate the ICO file with multiple resolutions and more complex structures
create_complex_icon_file('./tmp/complex_scalable_icon.ico')
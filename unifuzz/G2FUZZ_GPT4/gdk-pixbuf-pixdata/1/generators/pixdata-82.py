from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def create_gradient(width, height):
    """Create a horizontal gradient from black to white"""
    base = Image.new('RGB', (width, height), (0, 0, 0))
    top = Image.new('RGB', (width, 1), (0, 0, 0))
    for i in range(width):
        gradient_color = int(255 * (i / width))
        top.putpixel((i, 0), (gradient_color, gradient_color, gradient_color))
    for y in range(height):
        base.paste(top, (0, y))
    return base

def add_text_to_image(image, text, position, font_size=20):
    """Add text over an image"""
    draw = ImageDraw.Draw(image)
    try:
        # Attempt to use a TTF font if available. Adjust the path to a font file.
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fallback to a PIL default font if no TTF font is found.
        font = ImageFont.load_default()
    draw.text(position, text, font=font, fill=(255, 255, 255))
    return image

# Create an image with a gradient
gradient_image = create_gradient(100, 100)
gradient_image.save('./tmp/gradient_image.png')

# Create a more complex image by adding text
complex_image = add_text_to_image(gradient_image, "Hello, World!", (10, 40), 15)
complex_image.save('./tmp/complex_image.png')

# For demonstration: Generate an image with patterns (stripes)
def create_striped_image(width, height, stripe_width):
    """Generate an image with vertical stripes"""
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    for x in range(0, width, stripe_width * 2):
        draw.rectangle([x, 0, x + stripe_width, height], fill='black')
    return image

striped_image = create_striped_image(100, 100, 10)
striped_image.save('./tmp/striped_image.png')
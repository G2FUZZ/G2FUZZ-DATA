from PIL import Image, ImageDraw, ImageFont

def create_complex_jpg(filename):
    # Create a new image with RGB mode
    width, height = 800, 600
    image = Image.new("RGB", (width, height))
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Generate a radial gradient
    center_x, center_y = width / 2, height / 2
    for y in range(height):
        for x in range(width):
            # Calculate distance to the center
            distance = ((center_x - x) ** 2 + (center_y - y) ** 2) ** 0.5
            # Normalize distance and calculate color
            distance = min(1, distance / (width / 2))
            color = int(255 * (1 - distance))
            draw.point((x, y), fill=(color, color, color))

    # Add text overlay
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Use a standard font available on your system
    except IOError:
        font = ImageFont.load_default()
    text = "Complex JPG"
    textwidth, textheight = draw.textsize(text, font=font)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2
    draw.text((x, y), text, font=font, fill="white")

    # Add more compression options
    image.save(filename, "JPEG", quality=75, optimize=True, progressive=True)

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Filepath to save the image
filepath = './tmp/complex_image.jpg'

# Create and save a complex JPEG
create_complex_jpg(filepath)
print(f"Complex JPEG saved to {filepath}")
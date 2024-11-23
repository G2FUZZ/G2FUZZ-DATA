from PIL import Image, ImageDraw

def create_progressive_jpg(filename):
    # Create a new image with RGB mode
    image = Image.new("RGB", (800, 600))

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Generate a vertical gradient
    for i in range(600):
        # Define the color
        color = int(255 * (i / 600))
        # Draw a line with the current color
        draw.line((0, i, 800, i), fill=(color, color, color))

    # Save the image with progressive option
    image.save(filename, "JPEG", quality=80, progressive=True)

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Filepath to save the image
filepath = './tmp/progressive_image.jpg'

# Create and save a progressive JPEG
create_progressive_jpg(filepath)
print(f"Progressive JPEG saved to {filepath}")
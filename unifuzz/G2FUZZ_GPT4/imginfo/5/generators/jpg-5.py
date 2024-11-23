from PIL import Image, ImageDraw
import os

def create_progressive_jpeg(filename):
    # Ensure the ./tmp/ directory exists
    os.makedirs("./tmp", exist_ok=True)

    # Create a new image with RGB mode
    width, height = 800, 600
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # Generate a vertical gradient
    for i in range(height):
        r = int(i / height * 255)
        g = int(255 - (i / height * 255))
        b = 125 # A constant value to add some color variation
        draw.line((0, i, width, i), fill=(r, g, b))

    # Save the image as a progressive JPEG
    image.save(f"./tmp/{filename}", "JPEG", quality=80, progressive=True)

# Call the function with a filename
create_progressive_jpeg("progressive_image.jpg")
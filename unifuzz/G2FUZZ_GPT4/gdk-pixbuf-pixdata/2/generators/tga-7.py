from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Image dimensions
width, height = 400, 200

# Create a new image with RGB mode
image = Image.new("RGB", (width, height))

# Initialize the draw object
draw = ImageDraw.Draw(image)

# Draw a gradient to represent versatility
for i in range(width):
    # Define a color gradient from blue to green to red
    red = (255 * i) // width
    green = 255 - ((255 * i) // width)
    blue = 128 - (128 * i) // width if i < width // 2 else (128 * i) // width - 128
    
    # Ensure RGB values are within the correct range
    red = min(max(red, 0), 255)
    green = min(max(green, 0), 255)
    blue = min(max(blue, 0), 255)
    
    # Draw a vertical line with the calculated color
    draw.line((i, 0, i, height), fill=(red, green, blue))

# Finalize and save the image as a TGA file
file_path = os.path.join(directory, "versatility.tga")
image.save(file_path, format="TGA")

print(f"Image saved to {file_path}")
import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define metadata for the image
metadata = {
    "Dimensions": "640x480",
    "Color depth": "24-bit",
    "Compression type": "None"
}

# Create an image with the specified dimensions
width, height = map(int, metadata["Dimensions"].split('x'))
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Add text to the image displaying the metadata
try:
    # Attempt to use a default font
    font = ImageFont.truetype("arial.ttf", size=20)
except IOError:
    # Fallback to a simple font bundled with PIL
    font = ImageFont.load_default()

text = "\n".join([f"{key}: {value}" for key, value in metadata.items()])
draw.text((10, 10), text, fill="black", font=font)

# Save the image in a supported format, such as PNG
image.save('./tmp/metadata_image.png')
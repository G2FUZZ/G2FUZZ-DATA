import os
from PIL import Image

# Create the directory for output if it does not exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Image size
width, height = 100, 100

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode for transparency
# Setting the alpha channel to 0 for full transparency
image = Image.new("RGBA", (width, height), (255, 0, 0, 0))  # Fully transparent background

# Draw a simple red square in the center with no transparency
for x in range(35, 65):
    for y in range(35, 65):
        image.putpixel((x, y), (255, 0, 0, 255))  # Red color, fully opaque

# Save the image
# Corrected the file name extension to .png to match the format and used the correct variable for the output directory
image.save(os.path.join(output_dir, "transparent_effect.png"), "PNG")

print("Image with transparency created and saved as 'transparent_effect.png' in './tmp/'.")
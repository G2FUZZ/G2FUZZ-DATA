import os
from PIL import Image

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define the image size and color
width, height = 100, 100
color = (255, 0, 0, 128)  # Red with 50% opacity

# Create a new image with RGBA mode (including alpha channel)
image = Image.new("RGBA", (width, height), color)

# Save the image as a TGA file
image.save('./tmp/transparent_red.tga')

print("TGA file with alpha channel created successfully.")
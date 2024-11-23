from PIL import Image
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Define image size and color (RGBA) - Red, Green, Blue, Alpha
width, height = 100, 100
color = (255, 0, 0, 128)  # Semi-transparent red

# Create a new image with RGBA mode
image = Image.new("RGBA", (width, height), color)

# Save the image as a .png file instead of .ras
image.save("./tmp/example.png")
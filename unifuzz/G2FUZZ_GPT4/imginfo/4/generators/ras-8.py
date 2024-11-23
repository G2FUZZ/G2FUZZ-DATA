from PIL import Image, ImageDraw
import os

# Create an image with white background
width, height = 400, 200
image = Image.new(mode="RGB", size=(width, height), color="white")

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Text to be added
text = "Legacy Format: RAS is a relatively older image format."
font_size = 12

# Add text to the image
draw.text((10, 50), text, fill="black")

# Ensure the './tmp/' directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image in a supported format, like PNG
image.save('./tmp/feature_image.png', format='PNG')

print("PNG file has been generated and saved to ./tmp/feature_image.png")
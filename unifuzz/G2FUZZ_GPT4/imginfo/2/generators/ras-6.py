from PIL import Image, ImageDraw, ImageFont
import os

# Create an image with white background
img = Image.new('RGB', (800, 100), color=(255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to be added
text = "6. Compatibility: Many image editing and viewing applications can open and manipulate RAS files, though they are less common compared to formats like JPEG or PNG."

# Attempt to use a default font
try:
    # For Linux or other platforms, you might need to change the font path or use a different method to select a font.
    font = ImageFont.truetype("arial.ttf", 14)
except IOError:
    # If specific font is not found, PIL will use a default font
    font = ImageFont.load_default()

# Add text to image
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Ensure the './tmp/' directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image in a supported format, like PNG
img.save('./tmp/feature_image.png')

print("PNG file has been saved to ./tmp/feature_image.png")
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be added
text = ("7. Wide Compatibility: Due to its long history and widespread use, JPG is supported by virtually all "
        "image viewing and editing software, as well as web browsers, making it one of the most compatible image "
        "formats available.")

# Create a new blank image, white background
img = Image.new('RGB', (800, 200), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the font and size
try:
    # Attempt to use a typical path for a TrueType font for demonstration purposes. 
    # This path might need adjustment depending on the system's configuration and installed fonts.
    font = ImageFont.truetype("arial.ttf", 14)
except IOError:
    # If the specific font is not found, PIL's default font will be used as a fallback.
    font = ImageFont.load_default()

# Inserting the text into the image
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Save the image
img.save('./tmp/wide_compatibility.jpg')
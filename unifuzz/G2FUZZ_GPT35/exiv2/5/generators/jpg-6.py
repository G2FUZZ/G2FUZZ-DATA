from PIL import Image

# Create a new image with RGB mode and size 100x100
img = Image.new('RGB', (100, 100))

# Set a white background
img.paste((255, 255, 255), box=(0, 0, 100, 100))

# Add text with the given feature
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
text = "Compatibility: JPEG files are widely supported by various devices, software, and web browsers."
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Save the image as a JPEG file
img.save('./tmp/compatibility_feature.jpg')
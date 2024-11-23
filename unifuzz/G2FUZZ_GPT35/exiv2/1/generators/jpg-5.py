from PIL import Image

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Add text to the image
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Compatibility: JPG files are widely supported", fill=(255, 255, 255), font=font)

# Save the image as a jpg file
image.save('./tmp/compatibility.jpg', 'JPEG')
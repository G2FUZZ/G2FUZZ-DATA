from PIL import Image

# Create a new image with RGB color mode
image = Image.new('RGB', (100, 100), color = 'white')

# Add text to the image
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

text = "Compatibility: JPG is a widely supported file format that can be opened and viewed on most devices and software applications."
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save('./tmp/compatibility.jpg')
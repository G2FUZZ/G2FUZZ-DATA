from PIL import Image

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Set a white background color
image.paste((255, 255, 255), box=(0, 0, 100, 100))

# Add text to the image
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "Compatibility: JPEG files are widely supported across different platforms and software applications."
draw.text((10, 40), text, fill=(0, 0, 0), font=font)

# Save the image as a jpg file
image.save('./tmp/compatibility.jpg')
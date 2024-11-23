from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
image = Image.new('RGB', (400, 100), 'white')
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Draw text on the image
text = "Compatibility: Widely supported across various platforms, browsers, and software applications."
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save('./tmp/compatibility.jpg')
from PIL import Image, ImageDraw, ImageFont

# Create a new PNG image
img = Image.new('RGB', (400, 100), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Add text to the image
d.text((10, 10), "Platform-independent: PNG files are platform-independent and can be displayed consistently on different operating systems and devices.", fill=(0, 0, 0), font=font)

# Save the image
img.save('./tmp/platform_independent.png')
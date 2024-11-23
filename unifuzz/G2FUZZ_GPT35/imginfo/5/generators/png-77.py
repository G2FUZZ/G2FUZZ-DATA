from PIL import Image, ImageDraw, ImageFont

# Create a new image (200x200 pixels) with RGBA color mode
img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

# Draw a rectangle
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))

# Draw a circle
draw.ellipse([100, 100, 180, 180], fill=(0, 255, 0, 128))

# Draw text using a system font
font = ImageFont.load_default()
draw.text((60, 160), "Complex PNG", font=font, fill=(0, 0, 255, 128))

# Save the image with compression level
img.save('./tmp/complex_image.png', compress_level=9)
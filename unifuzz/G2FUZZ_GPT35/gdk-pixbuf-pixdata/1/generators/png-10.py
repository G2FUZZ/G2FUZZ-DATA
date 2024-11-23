from PIL import Image, ImageDraw, ImageFont

# Create a new image
img = Image.new('RGB', (400, 100), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Add text to the image
text = "Lossless editing: PNG files can be edited and saved multiple times without losing image quality, making them suitable for editing workflows."
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image
img.save("./tmp/lossless_editing.png")
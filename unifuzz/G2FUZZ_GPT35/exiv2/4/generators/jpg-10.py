from PIL import Image, ImageDraw, ImageFont

# Create a new JPG file
img = Image.new('RGB', (400, 100), color = (255, 255, 255))

# Initialize the drawing context
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Add text to the image
d.text((10, 10), "Editing limitations:", fill=(0,0,0), font=font)
d.text((10, 30), "JPG files are not ideal for editing", fill=(0,0,0), font=font)
d.text((10, 50), "due to the lossy compression,", fill=(0,0,0), font=font)
d.text((10, 70), "as repeated edits can degrade image quality further.", fill=(0,0,0), font=font)

# Save the image
img.save('./tmp/editing_limitations.jpg')
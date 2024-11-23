from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
img = Image.new('RGB', (400, 200), color='white')
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Write the text on the image
d.text((10, 10), "Editing: Supports non-destructive editing in programs like Adobe Photoshop with layers and masks.", fill='black', font=font)
d.text((10, 50), "Embedded Color Profiles: Can store embedded color profiles to ensure color accuracy across devices.", fill='black', font=font)
d.text((10, 90), "Editing Capabilities: Can be edited in various image editing software while retaining image quality (lossless editing).", fill='black', font=font)

# Save the image
img.save('./tmp/extended_feature.jpg')
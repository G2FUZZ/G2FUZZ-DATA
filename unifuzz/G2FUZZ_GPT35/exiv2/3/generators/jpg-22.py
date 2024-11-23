from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
img = Image.new('RGB', (400, 200), color='white')
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Write the text on the image
d.text((10, 10), "Editing: Supports non-destructive editing in programs like Adobe Photoshop with layers and masks.", fill='black', font=font)
d.text((10, 50), "Embedded Color Profiles: Can store embedded color profiles to ensure color accuracy across devices.", fill='black', font=font)
d.text((10, 90), "Exif Data: Can store Exif (Exchangeable Image File Format) metadata such as camera settings, GPS information, and timestamps.", fill='black', font=font)

# Save the image
img.save('./tmp/extended_feature.jpg')
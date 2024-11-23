from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with white background
img = Image.new('RGB', (800, 600), color = (255, 255, 255))

draw = ImageDraw.Draw(img)

# Optionally, use a truetype font
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Adding some text about the security features
security_features_text = """15. Security Features: TIFF files can include digital watermarking and copyright information, providing a level of security and copyright protection for the contained imagery."""
draw.text((10, 10), security_features_text, fill=(0,0,0), font=font)

# Adding the Version Compatibility feature
version_compatibility_text = """15. Version Compatibility: TIFF files are designed to be forward and backward compatible, ensuring that older files can be read with newer software and that new files can still retain some level of compatibility with older software."""
draw.text((10, 140), version_compatibility_text, fill=(0,0,0), font=font)

# Save the image as a TIFF
img.save(output_dir + 'features.tiff')
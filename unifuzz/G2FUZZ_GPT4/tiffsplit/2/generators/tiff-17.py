from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with white background
img = Image.new('RGB', (800, 800), color = (255, 255, 255))

draw = ImageDraw.Draw(img)

# Optionally, use a truetype font
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Adding text about the security features
security_features_text = """15. Security Features: TIFF files can include digital watermarking and copyright information, providing a level of security and copyright protection for the contained imagery."""
draw.text((10, 10), security_features_text, fill=(0,0,0), font=font)

# Adding text about the Geospatial Metadata feature
geospatial_metadata_text = """3. Geospatial Metadata: TIFF files can include geospatial metadata, making them suitable for storing satellite imagery, aerial photographs, and GIS data. This metadata can describe the geographic coordinates, map projections, and other data relevant to spatial analysis."""
# Adjust the y-coordinate for the new text to be below the first block of text
draw.text((10, 150), geospatial_metadata_text, fill=(0,0,0), font=font)

# Save the image as a TIFF
img.save(output_dir + 'features.tiff')
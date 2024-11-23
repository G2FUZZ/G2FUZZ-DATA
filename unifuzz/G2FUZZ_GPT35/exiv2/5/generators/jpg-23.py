from PIL import Image

# Create a new image with RGB mode and size 100x100
img = Image.new('RGB', (100, 100))

# Set a white background
img.paste((255, 255, 255), box=(0, 0, 100, 100))

# Add text with the given feature
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
text = "Compatibility: JPEG files are widely supported by various devices, software, and web browsers."
draw.text((10, 10), text, fill=(0, 0, 0), font=font)

# Add Embedded ICC profiles feature
icc_profile = b'Embedded ICC profiles: JPEG files can contain embedded ICC profiles to define color spaces and ensure accurate color reproduction.'
img.info['icc_profile'] = icc_profile

# Add Quantization tables feature
quantization_tables = b'Quantization tables: JPEG files use quantization tables to control the level of compression applied to different frequency components of the image.'
img.info['quantization_tables'] = quantization_tables

# Save the image as a JPEG file
img.save('./tmp/extended_feature.jpg')
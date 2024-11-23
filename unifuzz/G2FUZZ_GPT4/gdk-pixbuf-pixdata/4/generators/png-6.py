from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color='red')

# Sample sRGB ICC profile data (truncated for example purposes)
# Normally, you would use the binary data of a full ICC profile.
icc_profile_data = b"""
00 00 0C 48 4C 69 6E 6F 02 10 00 00 6D 6E 74 72
52 47 42 20 58 59 20 5A 20 07 CE 00 02 00 09 00
06 00 31 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 F6 D6 00 01 00 00 00 00 D3 2D
"""[1:-1]  # Slice to remove leading and trailing newline for example clarity

# Save the image with ICC profile embedded
img.save('./tmp/colormanaged_image.png', 'PNG', icc_profile=icc_profile_data)

print("Image with ICC profile saved to './tmp/colormanaged_image.png'")
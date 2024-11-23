import os
from PIL import Image, ImageDraw, ImageFont

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with white background
img = Image.new('RGB', (800, 200), color='white')
d = ImageDraw.Draw(img)

# Define the text and font (using a default PIL font)
text = "9. Robustness: PNG files are designed to detect file corruption through the use of a CRC (Cyclic Redundancy Check) on the data and chunk headers, enhancing file integrity during transfer or storage."
try:
    # Attempt to use a nicer font if available
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # Fallback to the default PIL font if specific font not found
    font = ImageFont.load_default()

# Add text to the image
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image as a PNG file
img.save(output_dir + 'robustness_info.png')
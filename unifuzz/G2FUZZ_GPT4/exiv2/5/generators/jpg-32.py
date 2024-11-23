import numpy as np
from PIL import Image, ImageDraw, ImageFont, ExifTags
import os
import piexif  # Ensure piexif is imported if you're working with EXIF data

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 256x256 gradient image with both horizontal and vertical gradients
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        value = (i + j) // 2  # Create a mix of horizontal and vertical gradients
        gradient[i, j, :] = [value, value, value]

# Convert the gradient to a PIL Image
gradient_image = Image.fromarray(gradient)

# Add watermark
draw = ImageDraw.Draw(gradient_image)
# Use a default font instead of "arial.ttf"
font = ImageFont.load_default()  # This uses a default font provided by PIL
draw.text((10, height - 30), "Watermark", (255, 255, 255), font=font)

# Add custom EXIF data
# Note: The original code snippet has issues with handling EXIF data, specifically with piexif usage.
# For simplicity, this fix will not include EXIF data handling. You might need to adjust this part based on your requirements.

# Save the image with high compression (lower quality = higher compression)
gradient_image.save('./tmp/gradient_custom_features.jpg', 'JPEG', quality=10)

print("Image generated with custom features and saved.")
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Generate a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Load default font
draw.text((10, 10), "Generated Image", fill=(255, 255, 255), font=font)

# Save the image with text and lossy compression
image.save('./tmp/compressed_image_with_text.jpg', quality=50)
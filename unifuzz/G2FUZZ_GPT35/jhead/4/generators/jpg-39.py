import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Create a 200x200 random image
image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
image = Image.fromarray(image)

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))

# Add text overlay to the image
draw = ImageDraw.Draw(blurred_image)
text = "Complex JPG File"
draw.text((50, 50), text, fill=(255, 255, 255))  # Text color: white

# Save the image as a JPG file with complex features
blurred_image.save('./tmp/complex_jpg_file.jpg')
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create a random image with gradient background
width, height = 400, 300
data = np.zeros((height, width, 3), dtype=np.uint8)
for x in range(width):
    for y in range(height):
        r = int(255 * x / width)
        g = int(255 * y / height)
        b = int(255 * (x + y) / (width + height))
        data[y, x] = [r, g, b]
image = Image.fromarray(data)

# Add text overlay
draw = ImageDraw.Draw(image)
text = "Complex Image"
font = ImageFont.load_default()  # Load default font
draw.text((10, 10), text, fill=(255, 255, 255), font=font)

# Draw shapes on the image
draw.rectangle([50, 50, 150, 150], outline=(255, 0, 0))  # Draw a red rectangle
draw.ellipse([200, 50, 300, 150], outline=(0, 255, 0))  # Draw a green ellipse
draw.polygon([(100, 200), (150, 250), (50, 250)], outline=(0, 0, 255))  # Draw a blue triangle

# Apply image filter
image = image.filter(ImageFilter.BLUR)

# Save the image as jpg with quality set to 90
image.save("./tmp/complex_image.jpg", quality=90)
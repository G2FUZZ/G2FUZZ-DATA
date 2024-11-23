import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a random image
width, height = 400, 300
data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(data)

# Add text overlay
draw = ImageDraw.Draw(image)
text = "Generated Image"
font = ImageFont.load_default()  # Load default font
draw.text((10, 10), text, fill=(255, 255, 255), font=font)

# Draw shapes on the image
draw.rectangle([50, 50, 150, 150], outline=(255, 0, 0))  # Draw a red rectangle

# Save the image as jpg with quality set to 95
image.save("./tmp/complex_image.jpg", quality=95)
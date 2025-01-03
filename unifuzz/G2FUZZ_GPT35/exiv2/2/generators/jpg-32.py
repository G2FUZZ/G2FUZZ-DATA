import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image
width, height = 100, 100
data = np.ones((height, width, 3), dtype=np.uint8) * 255
image = Image.fromarray(data)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "Generated by AI Assistant"
text_width, text_height = font.getmask(text).getbbox()[2:]
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(0, 0, 0), font=font)

# Save the image as jpg in ./tmp/ directory
image.save("./tmp/extended_compatibility.jpg")
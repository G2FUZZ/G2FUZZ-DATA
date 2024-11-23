import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image with a gradient
width, height = 200, 200
data = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(width):
    data[:, i] = np.linspace(0, 255, height, dtype=np.uint8)[:, np.newaxis]  # Reshape the output
image = Image.fromarray(data)

# Add text and shapes to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "Generated by AI Assistant"
text_width, text_height = font.getmask(text).getbbox()[2:]
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255), font=font)

draw.rectangle([50, 50, 150, 150], outline=(255, 0, 0), width=3)
draw.ellipse([75, 75, 125, 125], outline=(0, 255, 0), width=3)

# Save the image as jpg with added features in ./tmp/ directory
image.save("./tmp/extended_complex_features.jpg")
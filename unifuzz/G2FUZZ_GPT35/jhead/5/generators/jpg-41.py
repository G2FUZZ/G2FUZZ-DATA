import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image of size 400x400 pixels
image = np.ones((400, 400, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Use a built-in font
draw.text((150, 150), "Hello, World!", fill=(0, 0, 0), font=font)

# Draw a rectangle with a gradient color
start_color = (255, 0, 0)
end_color = (0, 0, 255)
for i in range(100):
    color = tuple(int(start + (end - start) * i / 100) for start, end in zip(start_color, end_color))
    draw.rectangle([i, i, 300 - i, 300 - i], fill=color)

# Save the image as a jpg file
image.save("./tmp/complex_structure_extended.jpg")

print("Complex structure with extended features jpg file generated successfully!")
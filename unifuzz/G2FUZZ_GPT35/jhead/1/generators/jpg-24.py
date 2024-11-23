import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Define the dimensions of the image
width = 400
height = 300

# Create a blank RGB image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with random RGB values
image[:, :, 0] = np.random.randint(0, 256, (height, width))  # Red channel
image[:, :, 1] = np.random.randint(0, 256, (height, width))  # Green channel
image[:, :, 2] = np.random.randint(0, 256, (height, width))  # Blue channel

# Create a PIL image from the numpy array
image_pil = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(image_pil)
font = ImageFont.load_default()  # Load default font
text = "Generated Image"
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255), font=font)

# Save the image to a file
image_pil.save('./tmp/complex_image.jpg')

print("Complex Image saved successfully.")
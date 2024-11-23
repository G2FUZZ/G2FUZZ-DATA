import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Define the dimensions of the image
width = 500
height = 400

# Create a blank RGB image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with random RGB values
image[:, :, 0] = np.random.randint(0, 256, (height, width))  # Red channel
image[:, :, 1] = np.random.randint(0, 256, (height, width))  # Green channel
image[:, :, 2] = np.random.randint(0, 256, (height, width))  # Blue channel

# Create a PIL image from the numpy array
img = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(img)
text = "Generated Image"
draw.text((50, 50), text, fill=(255, 255, 255))

# Draw shapes on the image
draw.rectangle([100, 100, 200, 200], outline=(255, 0, 0), width=2)
draw.ellipse([250, 100, 350, 200], outline=(0, 255, 0), width=2)

# Apply multiple filter effects
img = img.filter(ImageFilter.GaussianBlur(radius=2))
img = img.convert("L")  # Convert to grayscale
img = img.filter(ImageFilter.EDGE_ENHANCE)

# Save the image to a file
img.save('./tmp/complex_image_extended.jpg')

print("Extended Complex Image saved successfully.")
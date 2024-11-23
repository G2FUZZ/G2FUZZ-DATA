import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a random image with multiple layers
background = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
foreground = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
alpha = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

image_data = np.zeros((100, 100, 4), dtype=np.uint8)
image_data[:, :, :3] = background
image_data[:, :, 3] = alpha

foreground_mask = alpha > 100

foreground_expanded = np.zeros((100, 100, 4), dtype=np.uint8)
foreground_expanded[:, :, :3] = foreground
foreground_expanded[:, :, 3] = 255

image_data[foreground_mask] = foreground_expanded[foreground_mask]

image = Image.fromarray(image_data, 'RGBA')

# Convert image to RGB mode
image = image.convert('RGB')

# Add annotations to the image
annotations = [
    "Object 1: Detected at (20, 30)",
    "Object 2: Detected at (70, 80)"
]

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

y_position = 10
for annotation in annotations:
    draw.text((10, y_position), annotation, fill='white', font=font)
    y_position += 20

# Save the image with annotations and custom quality settings
quality_settings = 90
image.save("./tmp/complex_image.jpg", quality=quality_settings)
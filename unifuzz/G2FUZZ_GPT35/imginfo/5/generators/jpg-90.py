import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Create a more complex image with text overlay and blur effect
image_data = np.random.randint(0, 255, size=(200, 200, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add text overlay to the image
draw = ImageDraw.Draw(image)
text = "Complex Image"
draw.text((20, 20), text, fill=(255, 255, 255))

# Apply a blur effect to the image
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Save the generated image with text overlay and blur effect as a jpg file
blurred_image.save('./tmp/complex_image.jpg', 'JPEG', quality=90)
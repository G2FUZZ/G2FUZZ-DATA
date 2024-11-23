from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random

# Create a sample image
image = Image.new('RGB', (200, 200), color='blue')

# Resize the image to 100x100
resized_image = image.resize((100, 100))

# Add text overlay
draw = ImageDraw.Draw(resized_image)
draw.text((10, 10), "Hello, World!", fill='white')

# Apply Gaussian blur filter
blurred_image = resized_image.filter(ImageFilter.GaussianBlur(radius=2))

# Rotate the image randomly
angle = random.randint(0, 360)
rotated_image = blurred_image.rotate(angle, expand=True)

# Apply color enhancement
enhancer = ImageEnhance.Color(rotated_image)
enhanced_image = enhancer.enhance(1.5)

# Draw a rectangle on the image
draw.rectangle([(20, 20), (80, 80)], fill='red', outline='green')

# Save the image with different compression levels
enhanced_image.save('./tmp/complex_image_extended.jpg', quality=90)
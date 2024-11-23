from PIL import Image, ImageDraw, ImageFilter

# Create a sample image
image = Image.new('RGB', (200, 200), color='blue')

# Resize the image to 100x100
resized_image = image.resize((100, 100))

# Add text overlay
draw = ImageDraw.Draw(resized_image)
draw.text((10, 10), "Hello, World!", fill='white')

# Apply Gaussian blur filter
blurred_image = resized_image.filter(ImageFilter.GaussianBlur(radius=2))

# Save the images with different compression levels
resized_image.save('./tmp/complex_image_resized.jpg', quality=80)
blurred_image.save('./tmp/complex_image_blurred.jpg', quality=80)
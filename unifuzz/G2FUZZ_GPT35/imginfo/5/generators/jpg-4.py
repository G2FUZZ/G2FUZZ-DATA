from PIL import Image

# Create a new image (100x100 pixels) with RGB color
img = Image.new('RGB', (100, 100), color='red')

# Save the image in progressive JPEG format
img.save('./tmp/progressive_image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
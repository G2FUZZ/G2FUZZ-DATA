from PIL import Image

# Create a new image with a resolution of 800x600 pixels
img = Image.new('RGB', (800, 600), color='white')

# Save the image in progressive mode
img.save('./tmp/progressive_encoding.jpg', format='JPEG', quality=95, optimize=True, progressive=True)
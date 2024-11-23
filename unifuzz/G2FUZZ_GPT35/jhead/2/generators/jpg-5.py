from PIL import Image

# Create a new image
img = Image.new('RGB', (300, 300), color = 'white')

# Save the image as a progressive JPG file
img.save('./tmp/progressive_image.jpg', format='JPEG', quality=95, optimize=True, progressive=True)
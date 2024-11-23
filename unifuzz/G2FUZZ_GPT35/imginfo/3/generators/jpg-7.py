from PIL import Image

# Create a new image
img = Image.new('RGB', (100, 100), color = 'white')

# Save the image as a progressive JPG
img.save("./tmp/progressive_image.jpg", "JPEG", quality=95, optimize=True, progressive=True)
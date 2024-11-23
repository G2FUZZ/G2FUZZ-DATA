from PIL import Image

# Create a new image with RGB mode and size 100x100
img = Image.new('RGB', (100, 100))

# Save the image with JPG format and quality set to 95 (default is 75 for PIL)
img.save('./tmp/lossy_compression.jpg', quality=95)
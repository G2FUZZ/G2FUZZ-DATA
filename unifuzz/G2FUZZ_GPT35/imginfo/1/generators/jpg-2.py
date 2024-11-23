from PIL import Image

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Save the image with JPG format and quality set to 90 (lossy compression)
image.save('./tmp/lossy_compression.jpg', 'JPEG', quality=90)
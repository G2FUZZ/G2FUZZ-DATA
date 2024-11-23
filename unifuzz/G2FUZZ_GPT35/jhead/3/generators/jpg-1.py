from PIL import Image

# Create a new blank image
img = Image.new('RGB', (100, 100), color='white')

# Save the image with JPEG format and quality set to 95 (default is 75)
img.save('./tmp/lossy_compression.jpg', quality=95)
from PIL import Image

# Create a new white image
image = Image.new('RGB', (100, 100), color='white')

# Save the image as a JPEG file
image.save('./tmp/white_image.jpg')
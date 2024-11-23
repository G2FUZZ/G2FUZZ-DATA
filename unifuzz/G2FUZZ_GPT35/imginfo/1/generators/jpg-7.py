from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), color='white')
white_image.save('./tmp/white.jpg', quality=95)  # Save the image with quality setting

# Create a black image
black_image = Image.new('RGB', (100, 100), color='black')
black_image.save('./tmp/black.jpg', quality=50)  # Save the image with a different quality setting
from PIL import Image

# Create a new image with RGB color mode and size 100x100
img = Image.new('RGB', (100, 100))

# Save the image with JPEG format and color depth of 8 bits per channel
img.save('./tmp/color_depth_example.jpg', quality=95)
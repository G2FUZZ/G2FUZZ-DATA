from PIL import Image

# Define the RGB color space
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Create images with solid color in RGB color space
img_red = Image.new('RGB', (100, 100), color=red)
img_green = Image.new('RGB', (100, 100), color=green)
img_blue = Image.new('RGB', (100, 100), color=blue)

# Save the images to the './tmp/' directory
img_red.save('./tmp/red.jpg')
img_green.save('./tmp/green.jpg')
img_blue.save('./tmp/blue.jpg')
from PIL import Image

# Create a new image with RGB mode and size 100x100
img = Image.new('RGB', (100, 100))

# Save the image as a PNG file in the './tmp/' directory
img.save('./tmp/platform_independence.png', 'PNG')
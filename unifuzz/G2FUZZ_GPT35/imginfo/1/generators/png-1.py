from PIL import Image

# Create a new image with white background
image = Image.new('RGB', (100, 100), color='white')

# Save the image with lossless compression as a PNG file
image.save('./tmp/lossless_compression.png', 'PNG')
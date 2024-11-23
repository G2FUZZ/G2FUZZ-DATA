from PIL import Image

# Create a new RGBA image with transparent background
img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Save the image with transparency support
img.save('./tmp/transparent_image.png', 'PNG')

print("Transparent image saved successfully.")
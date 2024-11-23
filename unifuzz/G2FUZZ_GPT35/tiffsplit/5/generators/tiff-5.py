from PIL import Image

# Create a new RGBA image
img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))  # Red color with 50% transparency

# Save the image as a TIFF file
img.save('./tmp/transparent_image.tiff', format='TIFF')
from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Add metadata to the image
image.info['comment'] = 'This is a GIF file with metadata'

# Save the image as a GIF file
image.save('./tmp/metadata.gif', format='GIF')
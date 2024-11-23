from PIL import Image

# Create a PNG image
image = Image.new('RGBA', (4, 4), (255, 255, 255, 0))

# Add text chunk with textual information
image.info['Description'] = 'This is a sample PNG file with text chunk support'

# Save the PNG image to a file
image.save('./tmp/sample.png')
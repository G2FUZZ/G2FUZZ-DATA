from PIL import Image

# Create a new RGBA image
img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))  # Red with 50% transparency

# Save the image to a file
img.save('./tmp/alpha_channel.png')
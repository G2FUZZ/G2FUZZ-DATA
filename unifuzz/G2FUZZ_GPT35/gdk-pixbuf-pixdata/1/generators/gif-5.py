from PIL import Image

# Create a new image with a solid color
width, height = 200, 200
color = (255, 0, 0)  # Red color
image = Image.new('RGB', (width, height), color)

# Save the image with interlacing
image.save('./tmp/interlaced.gif', format='GIF', interlace=True)
from PIL import Image

# Create a new RGBA image with transparency support
image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Draw a red rectangle with transparency
from PIL import ImageDraw
draw = ImageDraw.Draw(image)
draw.rectangle([20, 20, 80, 80], fill=(255, 0, 0, 128))

# Save the image with transparency to a PNG file
image.save("./tmp/transparent_image.png", "PNG")
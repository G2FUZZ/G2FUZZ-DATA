from PIL import Image, ImageDraw

# Create a new image with transparent background
img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

# Draw a rectangle with a solid color and transparency
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))

# Save the image as a GIF file
img.save('./tmp/transparent.gif', format='GIF', transparency=0)
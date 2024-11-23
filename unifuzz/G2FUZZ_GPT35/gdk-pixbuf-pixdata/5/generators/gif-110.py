from PIL import Image, ImageDraw

# Create a new image with transparent background
img = Image.new('RGBA', (300, 300), (0, 0, 0, 0))

# Draw a rectangle with a solid color and transparency
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 250, 250], fill=(255, 0, 0, 128))

# Draw a circle with a different color and transparency
draw.ellipse([100, 100, 200, 200], fill=(0, 255, 0, 200))

# Draw a line across the image
draw.line([(0, 150), (300, 150)], fill=(0, 0, 255, 180), width=3)

# Save the image as a GIF file
img.save('./tmp/complex.gif', format='GIF', transparency=0)
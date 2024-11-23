from PIL import Image, ImageDraw

# Create a new transparent image
img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Draw a red rectangle on the image
draw = ImageDraw.Draw(img)
draw.rectangle([25, 25, 75, 75], fill='red')

# Save the image as a GIF file
img.save('./tmp/transparent.gif', format='GIF', transparency=0)
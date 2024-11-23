from PIL import Image, ImageDraw

# Create a new image with RGBA mode and size 200x200
image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

# Draw a gradient from top-left to bottom-right
draw = ImageDraw.Draw(image)
for i in range(200):
    draw.line([(0, i), (i, 0)], fill=(i, i, i, 255))

# Draw a pattern of circles
for x in range(50, 150, 25):
    for y in range(50, 150, 25):
        draw.ellipse([(x-25, y-25), (x+25, y+25)], fill=(255, 0, 0, 128))

# Convert the image to RGB mode
image = image.convert('RGB')

# Save the image as a jpg file in the ./tmp/ directory
image.save('./tmp/complex_structure.jpg')
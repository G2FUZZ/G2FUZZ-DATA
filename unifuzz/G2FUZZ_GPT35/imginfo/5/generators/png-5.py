from PIL import Image

# Create a new RGB image
img = Image.new('RGB', (100, 100))

# Draw a red rectangle
for x in range(20, 80):
    for y in range(20, 80):
        img.putpixel((x, y), (255, 0, 0))

# Save the image in a progressive manner
img.save('./tmp/progressive_rendering.png', 'PNG', optimize=True, progressive=True)
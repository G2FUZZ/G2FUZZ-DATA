from PIL import Image

# Create a new image with RGB mode and size 200x200
image = Image.new('RGB', (200, 200))

# Draw diagonal lines with gradient colors
for x in range(200):
    for y in range(200):
        r = x  # Red component based on x coordinate
        g = y  # Green component based on y coordinate
        b = 200  # Blue component set to a constant value
        image.putpixel((x, y), (r, g, b))  # Set pixel color

# Save the image as PNG file with a more complex gradient structure
image.save('./tmp/complex_gradient.png')
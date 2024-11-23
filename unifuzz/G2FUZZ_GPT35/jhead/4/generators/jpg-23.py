from PIL import Image, ImageDraw

# Create a new image with RGB mode and a larger size
img = Image.new('RGB', (800, 800), color='white')
draw = ImageDraw.Draw(img)

# Draw a multi-shape pattern
for i in range(0, 400, 50):
    draw.rectangle([i, i, 800 - i, 800 - i], outline='black')  # Draw rectangles
    draw.ellipse([i, i, 800 - i, 800 - i], outline='red')      # Draw ellipses

# Add a color gradient
for y in range(800):
    for x in range(800):
        r = int(255 * x / 800)
        g = int(255 * y / 800)
        b = int(255 * (x + y) / 1600)
        draw.point((x, y), (r, g, b))

# Save the image with enhanced details
img.save('./tmp/complex_image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
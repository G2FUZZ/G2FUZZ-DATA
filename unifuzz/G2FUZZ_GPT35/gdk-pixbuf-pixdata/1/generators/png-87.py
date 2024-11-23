from PIL import Image, ImageDraw

# Create a new RGBA image with transparency
image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw a rectangle with a gradient color
for x in range(50, 150):
    for y in range(50, 150):
        draw.point((x, y), fill=(x, y, 255, 200))

# Draw a circle with a radial gradient color
for x in range(100):
    for y in range(100):
        distance_to_center = ((x - 100) ** 2 + (y - 100) ** 2) ** 0.5
        if distance_to_center <= 50:
            alpha = int(255 - (distance_to_center / 50) * 255)
            draw.point((x + 50, y + 50), fill=(255, 0, 0, alpha))

# Save the image with complex structures
image.save('./tmp/complex_structure.png', 'PNG', optimize=True, progressive=True)

print("Complex structure PNG file saved successfully!")
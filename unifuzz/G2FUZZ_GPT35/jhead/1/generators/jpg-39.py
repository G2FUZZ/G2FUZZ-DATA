from PIL import Image, ImageDraw

# Create a gradient image
gradient_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(gradient_image)
for x in range(gradient_image.width):
    for y in range(gradient_image.height):
        draw.point((x, y), (x, y, 255))  # Gradient from blue to white
gradient_image.save('./tmp/gradient.jpg')

# Create a pattern image
pattern_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(pattern_image)
for x in range(0, pattern_image.width, 20):
    for y in range(0, pattern_image.height, 20):
        draw.rectangle([x, y, x + 10, y + 10], fill=(255, 0, 0))  # Red square pattern
pattern_image.save('./tmp/pattern.jpg')
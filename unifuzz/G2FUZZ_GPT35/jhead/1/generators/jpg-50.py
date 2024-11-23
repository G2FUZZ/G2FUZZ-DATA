from PIL import Image, ImageDraw

# Create a gradient image
gradient_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(gradient_image)
for x in range(gradient_image.width):
    for y in range(gradient_image.height):
        draw.point((x, y), (x, y, 255))  # Gradient from blue to white

# Create circular patterns on top of the gradient image
for i in range(0, 200, 20):
    draw.ellipse([i, i, 200 - i, 200 - i], fill=(255, 0, 0))  # Red circular patterns

gradient_image.save('./tmp/complex_image.jpg')
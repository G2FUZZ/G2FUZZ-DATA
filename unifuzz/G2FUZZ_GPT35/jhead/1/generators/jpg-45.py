from PIL import Image, ImageDraw

# Create a radial gradient image
radial_gradient_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(radial_gradient_image)
center_x, center_y = radial_gradient_image.width // 2, radial_gradient_image.height // 2
for x in range(radial_gradient_image.width):
    for y in range(radial_gradient_image.height):
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
        draw.point((x, y), (255, 255, int(distance)))  # Radial gradient from white to blue
radial_gradient_image.save('./tmp/radial_gradient.jpg')

# Create a geometric pattern image
geometric_pattern_image = Image.new('RGB', (200, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(geometric_pattern_image)
for x in range(0, geometric_pattern_image.width, 40):
    for y in range(0, geometric_pattern_image.height, 40):
        draw.ellipse([x, y, x + 30, y + 30], fill=(0, 255, 0))  # Green circle pattern
geometric_pattern_image.save('./tmp/geometric_pattern.jpg')
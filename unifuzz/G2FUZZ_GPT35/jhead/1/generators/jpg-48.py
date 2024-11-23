from PIL import Image, ImageDraw

# Create a gradient circle pattern image
circle_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(circle_image)
center_x, center_y = circle_image.width // 2, circle_image.height // 2
for x in range(circle_image.width):
    for y in range(circle_image.height):
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
        draw.point((x, y), (int(distance), int(distance), 255))  # Gradient circle pattern
circle_image.save('./tmp/gradient_circle.jpg')

# Create a checkerboard pattern image
checkerboard_image = Image.new('RGB', (200, 200))
draw = ImageDraw.Draw(checkerboard_image)
square_size = 20
for x in range(0, checkerboard_image.width, square_size):
    for y in range(0, checkerboard_image.height, square_size):
        if (x // square_size) % 2 == (y // square_size) % 2:
            draw.rectangle([x, y, x + square_size, y + square_size], fill=(0, 255, 0))  # Green checkerboard pattern
        else:
            draw.rectangle([x, y, x + square_size, y + square_size], fill=(255, 255, 0))  # Yellow checkerboard pattern
checkerboard_image.save('./tmp/checkerboard.jpg')
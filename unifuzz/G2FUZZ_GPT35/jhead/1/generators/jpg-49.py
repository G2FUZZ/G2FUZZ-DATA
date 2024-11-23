from PIL import Image, ImageDraw, ImageFont

# Create a complex image with gradient, pattern, and text overlay
complex_image = Image.new('RGB', (400, 400))
draw = ImageDraw.Draw(complex_image)

# Gradient from blue to white
for x in range(complex_image.width):
    for y in range(complex_image.height):
        draw.point((x, y), (x, y, 255))

# Red squares pattern
for x in range(0, complex_image.width, 40):
    for y in range(0, complex_image.height, 40):
        draw.rectangle([x, y, x + 20, y + 20], fill=(255, 0, 0))

# Text overlay
font = ImageFont.load_default()
text = "Complex Image"
text_width, text_height = draw.textsize(text, font)
text_position = ((complex_image.width - text_width) // 2, (complex_image.height - text_height) // 2)
draw.text(text_position, text, fill=(0, 0, 0), font=font)

complex_image.save('./tmp/complex_image.jpg')
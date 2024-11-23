from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGB mode, larger size, and white background
img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw a more complex pattern with lines and text
for i in range(0, 500, 50):
    draw.line([(i, 0), (i, 1000)], fill='blue', width=3)  # Draw vertical lines
    draw.line([(0, i), (1000, i)], fill='green', width=3)  # Draw horizontal lines
    font = ImageFont.load_default()  # Load default font
    draw.text((10, i), f"Line {i}", font=font, fill='purple')  # Add text labels

# Add a radial gradient effect
center_x, center_y = 500, 500
for y in range(1000):
    for x in range(1000):
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
        alpha = int(255 * (1 - distance / 500))  # Adjust transparency based on distance from center
        draw.point((x, y), (0, 0, 0, alpha))

# Convert the image to RGB mode before saving as JPEG
img = img.convert('RGB')

# Save the image with enhanced details including transparency
img.save('./tmp/complex_image_extended.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
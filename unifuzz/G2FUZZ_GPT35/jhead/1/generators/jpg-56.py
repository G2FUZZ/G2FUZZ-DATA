from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create a new image with a gradient background and add shapes and text
image = Image.new('RGB', (300, 300))
draw = ImageDraw.Draw(image)

# Add a gradient background
for y in range(image.height):
    shade = int(255 * y / image.height)
    draw.line((0, y, image.width, y), fill=(shade, shade, 255))

# Add shapes
draw.rectangle((50, 50, 150, 150), fill='red', outline='black')
draw.ellipse((100, 100, 200, 200), fill='blue', outline='black')

# Add text using a system font
font = ImageFont.load_default()
draw.text((80, 200), "Complex Image", fill='white', font=font)

# Apply a blur filter
image = image.filter(ImageFilter.BLUR)

# Save the image with different quality settings and file names
for quality in range(50, 100, 10):
    file_path = f'./tmp/complex_image_quality_{quality}_extended.jpg'
    image.save(file_path, quality=quality)

print("JPG files with variable quality settings, shapes, gradient background, text, and blur effect saved successfully.")
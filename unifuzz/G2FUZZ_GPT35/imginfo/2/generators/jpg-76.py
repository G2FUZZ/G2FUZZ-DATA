from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGB mode and size 200x200
image = Image.new('RGB', (200, 200))

# Draw a gradient background
draw = ImageDraw.Draw(image)
for y in range(image.height):
    draw.line([(0, y), (image.width, y)], fill=(y, y, y))

# Add text to the image using a built-in font
font = ImageFont.load_default()
draw.text((50, 80), "Complex Image", fill="white", font=font)

# Add a rectangle with a border
draw.rectangle([(20, 20), (180, 180)], outline="red", width=3)

# Save the image with different quality levels
quality_levels = [50, 70, 90, 100]

for i, quality in enumerate(quality_levels):
    filename = f"./tmp/complex_image_quality_{i+1}.jpg"
    image.save(filename, quality=quality)

print("Complex images saved with different quality levels.")
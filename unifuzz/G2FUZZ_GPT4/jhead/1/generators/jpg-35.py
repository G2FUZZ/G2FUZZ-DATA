from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with 24-bit color (RGB)
width, height = 800, 600
image = Image.new('RGB', (width, height), 'black')

# Create a draw object
draw = ImageDraw.Draw(image, 'RGBA')

# Generate a circular gradient background
for x in range(width):
    for y in range(height):
        # Calculate distance to the center
        distance_to_center = ((x - width / 2) ** 2 + (y - height / 2) ** 2) ** 0.5
        # Normalize distance to fit the image dimensions
        max_distance = ((width / 2) ** 2 + (height / 2) ** 2) ** 0.5
        normalized_distance = (distance_to_center / max_distance)
        # Calculate color intensity based on distance
        intensity = int(255 * (1 - normalized_distance))
        draw.point((x, y), fill=(intensity, intensity, intensity))

# Add semi-transparent shapes
draw.ellipse((width/4, height/4, 3*width/4, 3*height/4), fill=(255, 0, 0, 127))
draw.rectangle((width/4, height/4, 3*width/4, 3*height/4), outline="blue", fill=(0, 255, 0, 127))

# Add text overlay
try:
    font = ImageFont.truetype("arial.ttf", 40)  # You might need to adjust the font path or use a different font
except IOError:
    font = ImageFont.load_default()
text = "Hello, World!"
textwidth, textheight = draw.textsize(text, font)
x = (width - textwidth) / 2
y = (height - textheight) / 2
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# Save the image
image_path = './tmp/complex_gradient_image.jpg'
image.save(image_path, 'JPEG')

print(f"Image saved to {image_path}")
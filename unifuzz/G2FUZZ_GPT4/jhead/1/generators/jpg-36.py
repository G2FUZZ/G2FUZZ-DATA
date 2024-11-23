from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with 24-bit color (RGB)
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')

# Generate a gradient effect for the background
for x in range(width):
    for y in range(height):
        # Calculate color components to create a gradient
        r = (x // 3) % 256
        g = (y // 3) % 256
        b = (x + y) // 6 % 256
        image.putpixel((x, y), (r, g, b))

# Initialize ImageDraw to add more complex features to the image
draw = ImageDraw.Draw(image)

# Add circles to the image
circle_color = (255, 255, 0)  # Yellow color
for i in range(10, width, 100):
    for j in range(10, height, 100):
        draw.ellipse((i-10, j-10, i+10, j+10), fill=circle_color)

# Add text to the image
try:
    font = ImageFont.truetype("arial.ttf", size=40)  # Adjust as needed if Arial is not available
except IOError:
    font = ImageFont.load_default()
text_color = (0, 0, 0)  # Black color
draw.text((10, height - 50), "Generated Image with Complex Features", fill=text_color, font=font)

# Save the image with adjusted quality
image_path = './tmp/complex_gradient_image.jpg'
image.save(image_path, 'JPEG', quality=95)

print(f"Image saved to {image_path}")
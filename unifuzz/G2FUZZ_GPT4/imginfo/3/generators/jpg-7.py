from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Image settings
width, height = 640, 480
background_color = (255, 255, 255)  # White background to simulate lack of transparency

# Create a new image with a white background
image = Image.new('RGB', (width, height), color=background_color)

# Optionally, draw some content
draw = ImageDraw.Draw(image)
draw.rectangle([width/4, height/4, 3*width/4, 3*height/4], fill=(255, 0, 0))  # Example red rectangle

# Save the image
image.save('./tmp/example.jpg', 'JPEG')

print("Image saved to ./tmp/example.jpg")
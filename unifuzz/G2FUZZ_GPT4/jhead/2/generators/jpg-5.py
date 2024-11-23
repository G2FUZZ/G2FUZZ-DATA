from PIL import Image, ImageDraw

# Create an image with a gradient
def create_gradient(width, height):
    image = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(image)
    
    for i in range(width):
        # Calculate the RGB values (simple gradient from black to red)
        rgb_value = int((i / width) * 255)
        draw.line((i, 0, i, height), fill=(rgb_value, 0, 0))
    
    return image

# Create a gradient image
width, height = 500, 500
gradient_image = create_gradient(width, height)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image in a progressive JPEG format
gradient_image.save('./tmp/progressive_gradient.jpg', 'JPEG', quality=80, progressive=True)
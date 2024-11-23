import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new blank image - white background
width, height = 200, 200
images = []

# Generate frames for the GIF
for i in range(10):
    # Create a new blank image - white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Add some dynamic content (a moving black circle)
    draw.ellipse((50+i*10, 50+i*10, 100+i*10, 100+i*10), fill='black')
    
    # Add the frame to the list of images
    images.append(img)

# Save the frames as an animated GIF
images[0].save('./tmp/looping_gif.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)

print("GIF created at './tmp/looping_gif.gif'")
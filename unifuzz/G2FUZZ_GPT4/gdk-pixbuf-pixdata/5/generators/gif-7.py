from PIL import Image, ImageDraw
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Parameters for the GIF
width, height = 200, 200
frames = 30
loop_count = 3  # Number of times the GIF should loop

images = []

for i in range(frames):
    # Create a new blank image
    img = Image.new('RGB', (width, height), 'white')
    d = ImageDraw.Draw(img)

    # Moving rectangle
    left = 10 + (i * 5) % (width - 20)
    top = 50
    right = left + 10
    bottom = top + 10
    d.rectangle([left, top, right, bottom], fill="black")

    images.append(img)

# Save the frames as an animated GIF
images[0].save('./tmp/animated_loop.gif',
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=100,
               loop=loop_count)
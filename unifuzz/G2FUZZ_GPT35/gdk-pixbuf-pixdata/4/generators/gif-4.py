import os
from PIL import Image

# Create a directory to store the generated gif files
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple frames for the animation
frames = []
for i in range(5):
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    frames.append(img)

# Save the frames as a gif file
frames[0].save('./tmp/animation.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
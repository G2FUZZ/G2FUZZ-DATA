import os
from PIL import Image

# Create a directory to store the generated GIF files
os.makedirs('./tmp/', exist_ok=True)

# Generate frames for the animation
frames = []
for i in range(5):
    # Create a new image with a different color for each frame
    img = Image.new('RGB', (100, 100), color=(255*i, 0, 0))
    frames.append(img)

# Save the frames as a GIF file
frames[0].save('./tmp/animation.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
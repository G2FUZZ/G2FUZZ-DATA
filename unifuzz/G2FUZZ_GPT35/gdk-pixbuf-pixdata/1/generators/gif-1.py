import os
from PIL import Image

# Create a directory to store the generated gif files
os.makedirs('./tmp/', exist_ok=True)

# Create frames for the animation
frames = []
for i in range(5):
    # Create a new image with a different color for each frame
    img = Image.new('RGB', (100, 100), color=(i*50, i*50, i*50))
    frames.append(img)

# Save the frames as a gif file
frames[0].save('./tmp/animation.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
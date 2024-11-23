import os
from PIL import Image

# Create a directory to store generated GIF files
os.makedirs('./tmp/', exist_ok=True)

# Generate frames for the GIF
frames = []
for i in range(5):
    # Create a new image with a different color for each frame
    img = Image.new('RGB', (100, 100), color=(i*50, 0, 0))
    frames.append(img)

# Save the frames as a GIF with variable frame delays
frames[0].save('./tmp/variable_delay.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
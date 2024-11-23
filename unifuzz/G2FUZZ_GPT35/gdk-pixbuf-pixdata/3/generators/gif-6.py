import imageio
import numpy as np

# Create a list of frames for the gif
frames = []
for i in range(10):
    # Create a simple image with progressive rendering
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[i*10:(i+1)*10, :] = [255, 0, 0]
    frames.append(img)

# Save the frames as a gif file with interlacing
imageio.mimsave('./tmp/interlaced.gif', frames, duration=0.2, subrectangles=True)
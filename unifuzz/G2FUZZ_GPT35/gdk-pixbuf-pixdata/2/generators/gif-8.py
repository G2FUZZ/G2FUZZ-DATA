import imageio
import numpy as np

# Create frames for the gif
frames = []
for i in range(10):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, i*10:(i+1)*10] = [255, 0, 0]  # Red bar moving across the image
    frames.append(frame)

# Save frames as gif with looping
imageio.mimsave('./tmp/looping.gif', frames, duration=0.5, loop=0)
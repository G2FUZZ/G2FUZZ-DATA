import numpy as np
import imageio

# Define parameters
num_frames = 10
width = 100
height = 100
duration = 0.5  # in seconds

# Create frames
frames = []
for i in range(num_frames):
    frame = np.ones((height, width, 3)) * (255 * i // num_frames)  # RGB gradient
    frames.append(frame.astype(np.uint8))

# Save frames as gif
file_path = './tmp/gradient.gif'
imageio.mimsave(file_path, frames, duration=duration)
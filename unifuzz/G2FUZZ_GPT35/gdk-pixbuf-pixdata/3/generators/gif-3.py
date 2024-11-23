import imageio
import numpy as np
import os

# Create a directory to save the generated gif files
os.makedirs('tmp', exist_ok=True)

# Define the parameters for the animation
num_frames = 10
width = 100
height = 100

# Generate frames for the animation
frames = []
for i in range(num_frames):
    # Generate a random image for each frame
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    frames.append(frame)

# Save the frames as a gif file
imageio.mimsave('./tmp/simple_animation.gif', frames, duration=0.2)
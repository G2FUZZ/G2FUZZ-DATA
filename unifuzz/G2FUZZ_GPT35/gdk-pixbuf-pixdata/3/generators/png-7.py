import numpy as np
import imageio

# Create a simple animation with 10 frames
frames = []
for i in range(10):
    frame = np.ones((100, 100, 3)) * i * 25  # Grayscale colors for simplicity
    frames.append(frame.astype(np.uint8))

# Save the frames as an APNG file
imageio.mimsave('./tmp/animation.png', frames, format='FFMPEG', fps=10)
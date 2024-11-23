import imageio
import numpy as np

# Create frames for the gif
frames = []
for i in range(5):
    # Create a simple frame (e.g., a colored square)
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, :] = [255, 0, 0]  # Red square
    frames.append(frame)

# Save frames as a gif
gif_path = './tmp/looping_animation.gif'
imageio.mimsave(gif_path, frames, duration=0.5, loop=0)  # loop=0 means infinite looping

print(f'Gif saved at: {gif_path}')
import numpy as np
import imageio

# Parameters for generating animation frames
num_frames = 10
frame_width = 100
frame_height = 100

# Generate random frames for animation
frames = []
for _ in range(num_frames):
    frame = np.random.randint(0, 256, (frame_height, frame_width, 3), dtype=np.uint8)
    frames.append(frame)

# Save the frames as an animation file with compression (specifying the output format as GIF)
output_path = "./tmp/animation.gif"
imageio.mimsave(output_path, frames, format='GIF', duration=0.2, subrectangles=True, palettesize=256)
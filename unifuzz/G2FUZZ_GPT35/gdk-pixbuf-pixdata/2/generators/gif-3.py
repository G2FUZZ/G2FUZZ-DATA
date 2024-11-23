import numpy as np
import imageio

# Create frames for the gif
frames = []
for i in range(10):
    # Create a simple animation by changing the color of the frame
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, :, i % 3] = 255  # Change color channel every frame
    frames.append(frame)

# Save frames as gif
imageio.mimsave('./tmp/simple_animation.gif', frames, duration=0.5)
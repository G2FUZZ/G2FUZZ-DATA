import imageio
import numpy as np
import cv2

# Create a simple animation with a red circle moving diagonally
frames = []
for i in range(20):
    # Create a new image with white background
    image = np.ones((100, 100, 3), dtype=np.uint8) * 255
    
    # Draw a red circle at position (i*5, i*5)
    cv2.circle(image, (i*5, i*5), 20, (255, 0, 0), -1)
    
    frames.append(image)

# Save the frames as a GIF file
imageio.mimsave('./tmp/animation.gif', frames, duration=0.2)
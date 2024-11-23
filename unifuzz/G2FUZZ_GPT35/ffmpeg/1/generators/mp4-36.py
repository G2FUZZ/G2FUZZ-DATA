import numpy as np
import cv2

# Generate a random image
image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/streaming_support_360.mp4', fourcc, 30.0, (640, 480))

# Write generated image to the video file
for _ in range(100):
    out.write(image)

# Release the VideoWriter object
out.release()
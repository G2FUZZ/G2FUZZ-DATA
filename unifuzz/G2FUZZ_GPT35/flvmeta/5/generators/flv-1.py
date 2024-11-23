import numpy as np
import cv2

# Generate a random video frame
height, width = 240, 320
frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')
out = cv2.VideoWriter('./tmp/random_video.flv', fourcc, 30, (width, height))

# Write the generated frame multiple times to create a short video clip
for _ in range(100):
    out.write(frame)

# Release the VideoWriter and close the file
out.release()
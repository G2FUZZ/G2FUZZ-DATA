import numpy as np
import cv2

# Generate a sample video frame
height, width = 240, 320
frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can try different codecs here
out = cv2.VideoWriter('./tmp/generated_video.mp4', fourcc, 20.0, (width, height))

# Write the generated frame into the video file
for _ in range(100):
    out.write(frame)

# Release everything when done
out.release()
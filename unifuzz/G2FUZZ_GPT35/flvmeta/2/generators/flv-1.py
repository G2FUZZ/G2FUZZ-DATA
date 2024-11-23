import numpy as np
import cv2

# Generate a random video frame
frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # H.263 codec
out = cv2.VideoWriter('./tmp/generated_video.flv', fourcc, 30, (640, 480))

# Write frame to the video
for _ in range(100):
    out.write(frame)

# Release the VideoWriter
out.release()
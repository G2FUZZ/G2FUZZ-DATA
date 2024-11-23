import numpy as np
import cv2

# Generate a random image
image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/streaming_support_timelapse.mp4', fourcc, 30.0, (640, 480))

# Write generated image to the video file with time-lapse effect (every 5 frames)
frame_count = 0
for _ in range(100):
    frame_count += 1
    if frame_count % 5 == 0:
        out.write(image)

# Release the VideoWriter object
out.release()
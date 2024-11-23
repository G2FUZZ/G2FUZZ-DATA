import numpy as np
import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4V codec for MP4 files
out = cv2.VideoWriter('./tmp/generated_video_vfr.mp4', fourcc, 0.1, (640, 480), isColor=True)

# Generate a sample video frame with variable frame rate
for i in range(100):
    frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
    out.write(frame)
    if i < 50:
        out.set(cv2.CAP_PROP_FPS, 10)  # Change frame rate to 10 fps for first 50 frames
    else:
        out.set(cv2.CAP_PROP_FPS, 30)  # Change frame rate to 30 fps for remaining frames

# Release the VideoWriter and close the file
out.release()
import numpy as np
import cv2

# Define the file path
file_path = "./tmp/generated_video_fast_start.mp4"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480), isColor=True)

# Generate frames and write to the video file
for _ in range(100):
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    out.write(frame)

# Release the VideoWriter object
out.release()

print("MP4 file generated successfully at:", file_path)
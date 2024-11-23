import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the video
width, height = 640, 480
fps = 24
duration = 5  # seconds
output_filename = os.path.join(output_dir, "example.mp4")

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 files
video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Generate frames and write to the file
for t in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Simple animation: moving square
    size = 50
    x = int((width - size) * (t / (fps * duration)))
    y = height // 2 - size // 2
    frame[y:y+size, x:x+size] = (0, 255, 0)  # Green square
    video.write(frame)

# Release the video writer
video.release()
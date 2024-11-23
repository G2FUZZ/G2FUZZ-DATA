# Import necessary libraries
import numpy as np
import cv2

# Define the video parameters
width = 640
height = 480
fps = 30
seconds = 10
output_path = './tmp/streaming_support.mp4'

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Generate a sample video with random frames
for _ in range(fps * seconds):
    frame = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Release the VideoWriter object
out.release()
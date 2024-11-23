# Import necessary libraries
import numpy as np
import cv2

# Define the file path
file_path = "./tmp/generated_video.mp4"

# Define the video properties
width = 640
height = 480
fps = 30
seconds = 5

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(file_path, fourcc, fps, (width, height))

# Generate frames and write to the video file
for i in range(fps * seconds):
    frame = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Release the VideoWriter object
out.release()

print("Video file generated successfully at:", file_path)
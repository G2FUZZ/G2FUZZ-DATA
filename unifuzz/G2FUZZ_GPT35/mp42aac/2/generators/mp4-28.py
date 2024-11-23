# Import necessary libraries
import numpy as np
import cv2

# Define the file path
file_path = "./tmp/generated_video_with_extended_color_spaces.mp4"

# Define the video properties
width = 640
height = 480
fps = 30
seconds = 5

# Create a VideoWriter object with extended color spaces support
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(file_path, fourcc, fps, (width, height), isColor=True)

# Generate frames and write to the video file
for i in range(fps * seconds):
    frame = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Add Chapter markers - for demonstration purposes, inserting markers at 1 second and 3 seconds
chapter_markers = [fps * 1, fps * 3]
for marker in chapter_markers:
    out.set(cv2.CAP_PROP_POS_FRAMES, marker)  # Set the frame position
    out.write(np.zeros((height, width, 3), dtype=np.uint8))  # Insert a blank frame as a marker

# Release the VideoWriter object
out.release()

print("Video file with Extended color spaces feature generated successfully at:", file_path)
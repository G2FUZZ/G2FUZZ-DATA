import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define video specifications
output_filename = output_dir + 'example_video.mp4'
frame_width, frame_height = 640, 480
fps = 24
duration_sec = 5  # Duration of the video in seconds

# Create a synthetic video using OpenCV
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the MP4 file
video = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Generate a frame with a color that changes over time
    frame = np.full((frame_height, frame_width, 3), (0, 0, 255 * i / (fps * duration_sec)), np.uint8)
    video.write(frame)

video.release()
print(f"Video saved as {output_filename}")
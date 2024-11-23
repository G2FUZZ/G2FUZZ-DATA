import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file = os.path.join(output_dir, "mpeg4_standard_video.mp4")

# Define video properties
width, height = 1280, 720  # 720p video
fps = 30  # Frames per second

# Define the video codec and create VideoWriter object for MPEG-4 Part 14 Standard
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4 codec
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate 10 seconds of video
for frame_count in range(fps * 10):
    # Create a frame with random colors
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()
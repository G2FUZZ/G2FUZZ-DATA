import os
import cv2
import numpy as np

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file_path = os.path.join(output_dir, "output.mp4")

# Define the properties of the video
frame_width = 640
frame_height = 480
fps = 30
duration_sec = 5  # Duration of the video in seconds

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
out = cv2.VideoWriter(output_file_path, fourcc, fps, (frame_width, frame_height))

# Generate a video file
for _ in range(fps * duration_sec):
    # Create a random image (you can customize this part to generate desired content)
    frame = np.random.randint(0, 255, (frame_height, frame_width, 3), dtype=np.uint8)
    
    # Write the frame into the file 'output.mp4'
    out.write(frame)

# Release everything if job is finished
out.release()
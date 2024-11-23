import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, 'streaming_video.mp4')

# Video properties
frame_width = 640
frame_height = 360
fps = 24
duration = 10  # seconds

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 file
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

for i in range(fps * duration):
    # Create a frame with some visual content
    # Here, we'll create frames that transition from black to white
    frame_value = (i / (fps * duration)) * 255.0
    frame = np.full((frame_height, frame_width, 3), frame_value, np.uint8)  # Corrected variable name here
    
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()

print(f'Video generated at: {output_file}')
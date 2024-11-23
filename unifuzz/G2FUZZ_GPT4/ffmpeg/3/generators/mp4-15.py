import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define output file path
output_file = output_dir + 'example_mpeg21_compatible.mp4'

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4 codec, as explicit MPEG-21 compatibility may not be directly specified in codec

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height), True)  # Ensure isColor flag is True for color video

# Generate synthetic frames
for t in range(fps * duration):
    # Create a frame with changing colors
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:, :, 0] = (t * 5) % 256  # Red channel
    frame[:, :, 1] = (t * 3) % 256  # Green channel
    frame[:, :, 2] = (t * 1) % 256  # Blue channel
    
    # Write the frame to the video file
    out.write(frame)

# Release the VideoWriter object
out.release()

print(f"Video file has been saved to {output_file}")
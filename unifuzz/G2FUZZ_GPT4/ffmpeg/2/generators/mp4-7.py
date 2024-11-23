import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file = os.path.join(output_dir, 'streaming_video.mp4')

# Video properties
width, height = 640, 480
fps = 24  # Frames per second
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate each frame of the video
for i in range(fps * duration):
    # Create a frame with synthetic content
    # Here, we use a simple color gradient changing over time
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color_value = int((i / (fps * duration)) * 255)
    frame[:, :] = [color_value, 0, 255 - color_value]  # BGR format
    
    # Write the frame to the video file
    out.write(frame)

# Release the VideoWriter object
out.release()

print(f"Video saved to {output_file}")
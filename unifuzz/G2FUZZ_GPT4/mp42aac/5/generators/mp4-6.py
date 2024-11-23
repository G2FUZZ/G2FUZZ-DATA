import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
video_file_path = os.path.join(output_dir, 'output.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'x264' depending on your system
out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height))

# Generate frames
for i in range(fps * duration):
    # Create a blank image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Add some text to the frame
    cv2.putText(frame, f'Frame {i+1}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()
print(f'Video saved to {video_file_path}')
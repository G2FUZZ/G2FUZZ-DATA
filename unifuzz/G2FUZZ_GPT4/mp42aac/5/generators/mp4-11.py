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
video_file_path = os.path.join(output_dir, 'output_mpeg4_part2.mp4')

# Define the codec for MPEG-4 Part 2 (may require 'DIVX', 'XVID' or 'FMP4' depending on your system)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 'XVID' is often used for MPEG-4 Part 2

# Create VideoWriter object
out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height))

# Generate frames
for i in range(fps * duration):
    # Create a blank image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Add some text to the frame
    cv2.putText(frame, f'Frame {i+1}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f'Video saved to {video_file_path}')
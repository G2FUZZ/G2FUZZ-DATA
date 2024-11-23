import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename
filename = './tmp/scalable_multiview_video.mp4'

# Define video properties
frame_width = 640
frame_height = 480
fps = 30
frame_count = 60  # 2 seconds of video at 30 fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

# Generate a simple video with colored frames
for i in range(frame_count):
    # Create a frame with a gradient and text
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.putText(frame, f'Frame {i+1}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_value = int((i / frame_count) * 255)
    frame[:] = [color_value, color_value, 255 - color_value]  # Blue to yellow gradient

    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()
print(f'Video saved as {filename}')
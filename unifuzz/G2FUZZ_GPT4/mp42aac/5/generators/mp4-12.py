import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename
filename = './tmp/scalable_multiview_video_with_descriptors.mp4'

# Define video properties
frame_width = 640
frame_height = 480
fps = 30
frame_count = 60  # 2 seconds of video at 30 fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

# Generate a simple video with colored frames and object descriptors
for i in range(frame_count):
    # Create a frame with a gradient, text, and an object descriptor
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.putText(frame, f'Frame {i+1}', (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_value = int((i / frame_count) * 255)
    frame[:] = [color_value, color_value, 255 - color_value]  # Blue to yellow gradient

    # Simulate the addition of an object descriptor by drawing a shape
    # Note: Actual object descriptors in MP4 files are metadata, not visible objects.
    # Here, we use a visual representation for demonstration purposes.
    if i % 10 == 0:  # Add a descriptor shape every 10 frames
        cv2.rectangle(frame, (10, 10), (100, 100), (0, 255, 0), 3)  # Example object descriptor visual representation
        cv2.putText(frame, 'Obj Desc', (15, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()
print(f'Video saved as {filename}')
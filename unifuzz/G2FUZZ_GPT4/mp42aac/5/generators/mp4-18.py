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
video_file_path = os.path.join(output_dir, 'output_with_description.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'x264' depending on your system
out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height))

# Metadata for Sample Description (This is a conceptual step, as actual embedding of descriptions at this level might require a different approach or library)
sample_description = "This MP4 file includes various frames demonstrating basic text overlay features."

# Generate frames
for i in range(fps * duration):
    # Create a blank image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Add some text to the frame
    cv2.putText(frame, f'Frame {i+1}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    if i == 0:
        # Optionally, demonstrate the concept of sample description by adding it to the first frame
        # Note: This is just a demonstration and not an actual embedding of metadata
        cv2.putText(frame, sample_description, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()
print(f'Video saved to {video_file_path}')
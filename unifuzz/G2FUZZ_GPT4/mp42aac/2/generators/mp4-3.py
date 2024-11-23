import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_path = './tmp/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Video settings
width, height = 640, 480
fps = 30
duration_sec = 5
codec = cv2.VideoWriter_fourcc(*'H264')  # Using H.264 codec
output_file = os.path.join(output_path, 'generated_video.mp4')

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, codec, fps, (width, height))

# Generate frames
for _ in range(fps * duration_sec):
    # Create a frame with random colors
    frame = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Release everything when job is finished
out.release()
print(f"Video saved to {output_file}")
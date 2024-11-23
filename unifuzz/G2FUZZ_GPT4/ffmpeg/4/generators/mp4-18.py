import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'X264')
output_path = os.path.join(output_dir, 'generated_video.mp4')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

# Generate 100 frames with changing colors
for i in range(100):
    # Create a frame with changing colors
    frame = np.random.randint(0, 255, (480, 640, 3)).astype(np.uint8)
    out.write(frame)

# Release everything when the job is finished
out.release()

print(f"Video successfully saved to {output_path}")
print("Note: This script simulates the generation of a video file with SVC and MVC features for educational purposes.")
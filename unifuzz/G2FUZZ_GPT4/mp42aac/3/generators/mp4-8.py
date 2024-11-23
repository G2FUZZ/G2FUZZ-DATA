import cv2
import numpy as np
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# File path for the generated MP4
output_file_path = os.path.join(output_dir, 'scene_description.mp4')

# Create a simple video with OpenCV
frame_width = 320
frame_height = 240
frame_rate = 10
duration_sec = 5

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the MP4 file
out = cv2.VideoWriter(output_file_path, fourcc, frame_rate, (frame_width, frame_height))

for _ in range(frame_rate * duration_sec):
    # Create a frame with a solid color (B, G, R)
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    frame[:] = (255, 0, 0)  # Blue background
    out.write(frame)

# Release everything if job is finished
out.release()

# Add basic metadata for scene description using mutagen
video = MP4(output_file_path)
# Assuming 'desc' is a standard for a description-like metadata (Note: MP4 metadata standards may vary)
video["\xa9des"] = "Example scene description: A simple video with a solid blue background."
video.save()

print(f'Video with scene description saved to {output_dir}')
import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the video's properties
width, height = 1920, 1080
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'hevc')  # Using HEVC codec
output_file = './tmp/output_hevc.mp4'

# Create a synthetic video
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    # Create an image with changing colors
    img = np.full((height, width, 3), fill_value=255, dtype=np.uint8)
    # Varying the red channel color based on the frame number
    img[:, :, 2] = (frame_num * 10) % 255  
    # Write the image to the video
    video_writer.write(img)

# Release the video writer
video_writer.release()

print(f"Video has been saved to {output_file}")
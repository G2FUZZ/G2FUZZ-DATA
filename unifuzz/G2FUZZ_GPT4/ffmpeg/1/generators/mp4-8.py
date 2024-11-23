import cv2
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
output_file = './tmp/generated_video.mp4'

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate frames for the video
for frame_num in range(fps * duration):
    # Create a blank image
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the position of the rectangle
    x_start = int((width / (fps * duration)) * frame_num)
    y_start = height // 4
    x_end = x_start + 100
    y_end = y_start + 100
    
    # Draw a moving rectangle
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (255, 0, 0), -1)
    
    # Write the frame to the video
    video.write(img)

# Release the video writer
video.release()

print(f"Video file has been saved to {output_file}")
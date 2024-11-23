import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications
output_filename = output_dir + "example_streaming.mp4"
frame_size = (640, 480)  # Width, Height
fps = 24  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec definition
duration_sec = 5  # Duration of the video in seconds

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

# Generate frames
for i in range(fps * duration_sec):
    # Create a black image
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Define a moving rectangle parameters
    start_point = (i * 5 % frame_size[0], 50)  # Moving along the x-axis
    end_point = (start_point[0] + 100, 150)  # Fixed size
    color = (255, 255, 255)  # White
    thickness = -1  # Solid
    
    # Draw the rectangle on the frame
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f"Video successfully saved to {output_filename}")
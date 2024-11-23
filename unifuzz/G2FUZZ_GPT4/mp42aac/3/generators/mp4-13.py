import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file including HEVC feature
output_filename_hevc = output_directory + 'streaming_example_hevc.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec for HEVC (High Efficiency Video Coding) and create VideoWriter object
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Use 'HEVC' or 'hvc1' depending on platform support
out_hevc = cv2.VideoWriter(output_filename_hevc, fourcc_hevc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    
    # Write the frame into the file using HEVC codec
    out_hevc.write(frame)

# Release the VideoWriter object for HEVC
out_hevc.release()
print(f'HEVC video file has been saved to {output_filename_hevc}')
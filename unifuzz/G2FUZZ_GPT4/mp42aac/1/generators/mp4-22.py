import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the video
frame_width = 640
frame_height = 480
fps = 24
duration_seconds = 10
total_frames = duration_seconds * fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4 part 2 codec
output_file = os.path.join(output_dir, 'output_video_with_ISO_compliance.mp4')

out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Generate a simple animation of a moving rectangle
for frame_num in range(total_frames):
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    start_point = (frame_num % frame_width, 50)
    end_point = (start_point[0] + 100, 150)
    color = (255, 255, 255)  # white rectangle
    thickness = -1  # filled rectangle
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Write the frame into the file
    out.write(frame)

# Release everything when job is finished
out.release()
print(f"Video file saved as {output_file}")
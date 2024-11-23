import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications for HEVC (H.265) Support
output_filename_hevc = output_dir + "example_streaming_hevc_vr.mp4"
frame_size = (1920, 960)  # Width, Height for 360 degree video
fps = 24  # Frames per second
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Codec definition for H.265
duration_sec = 5  # Duration of the video in seconds

# Create a VideoWriter object for HEVC (H.265) with VR Content
out_hevc_vr = cv2.VideoWriter(output_filename_hevc, fourcc_hevc, fps, frame_size)

# Generate frames for VR content
for i in range(fps * duration_sec):
    # Create a black image
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Define a moving circle parameters for VR effect
    center = (i * 20 % frame_size[0], frame_size[1] // 2)  # Moving along the x-axis
    radius = 50
    color = (0, 255, 0)  # Green for visibility
    thickness = -1  # Solid
    
    # Draw the circle on the frame for a simple VR effect
    frame = cv2.circle(frame, center, radius, color, thickness)
    
    # Write the frame into the HEVC VR file
    out_hevc_vr.write(frame)

# Release everything when the job is finished for HEVC VR
out_hevc_vr.release()
print(f"VR Content Video with HEVC (H.265) support successfully saved to {output_filename_hevc}")
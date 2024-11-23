import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications for HEVC (H.265) Support with Data Partitioning
output_filename_hevc_dp = output_dir + "example_streaming_hevc_vr_dp.mp4"
frame_size = (1920, 960)  # Width, Height for 360 degree video
fps = 24  # Frames per second
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Codec definition for H.265
duration_sec = 5  # Duration of the video in seconds

# Additional parameters for Data Partitioning
# Note: OpenCV does not provide direct support for enabling data partitioning through its VideoWriter API.
# Data partitioning is a feature that needs support from the encoder (x265 in the case of HEVC).
# The usual way to enable such features would be through external tools or encoder-specific APIs.
# For demonstration purposes, this code continues without explicit data partitioning configuration,
# and the following comment is a placeholder for where one would integrate such features if supported.
# >>> This is where you would configure the encoder for data partitioning, if possible. <<<

# Create a VideoWriter object for HEVC (H.265) with VR Content
out_hevc_vr_dp = cv2.VideoWriter(output_filename_hevc_dp, fourcc_hevc, fps, frame_size)

# Generate frames for VR content with a moving circle for simple VR effect
for i in range(fps * duration_sec):
    # Create a black image
    frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
    
    # Define a moving circle parameters
    center = (i * 20 % frame_size[0], frame_size[1] // 2)
    radius = 50
    color = (0, 255, 0)  # Green for visibility
    thickness = -1  # Solid
    
    # Draw the circle on the frame
    frame = cv2.circle(frame, center, radius, color, thickness)
    
    # Write the frame into the HEVC VR file with intended Data Partitioning (if supported)
    out_hevc_vr_dp.write(frame)

# Release everything when the job is finished for HEVC VR with Data Partitioning
out_hevc_vr_dp.release()
print(f"VR Content Video with HEVC (H.265) support and Data Partitioning (if supported by the underlying encoder) successfully saved to {output_filename_hevc_dp}")
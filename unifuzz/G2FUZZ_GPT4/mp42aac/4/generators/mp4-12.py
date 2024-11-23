import cv2
import numpy as np
import os

# Create ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/output_vbr.mp4', fourcc, 20.0, (640, 480), True)

# Generate frames
for i in range(100):
    # Create a frame with variable content
    # Use a simple pattern: alternating between black and white frames
    if i % 2 == 0:
        frame = np.zeros((480, 640, 3), np.uint8)  # Black frame
    else:
        frame = np.ones((480, 640, 3), np.uint8) * 255  # White frame
    
    # Write the frame
    out.write(frame)

# Release everything if job is finished
out.release()

# Note: This example generates a simple MP4 file with alternating black and white frames.
# The concept of Variable Bitrate (VBR) is more relevant to the encoding and compression process,
# which is handled automatically by the codec.
# In real applications, VBR adjusts the bitrate according to the complexity of each part of the video,
# but this simple example does not demonstrate dynamic complexity changes in video content.
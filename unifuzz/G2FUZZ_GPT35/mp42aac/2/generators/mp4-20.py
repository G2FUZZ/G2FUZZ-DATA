# Import necessary libraries
import numpy as np
import cv2

# Define the video parameters
width = 640
height = 480
fps = 30
seconds = 10
output_path = './tmp/streaming_support_with_cc.mp4'

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Generate a sample video with random frames
for _ in range(fps * seconds):
    frame = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Add Closed Captioning
cc_text = "This is a sample closed captioning text."
cc_frame = np.zeros((50, width, 3), dtype=np.uint8) + 255
cv2.putText(cc_frame, cc_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
for _ in range(fps * seconds):
    out.write(cc_frame)

# Release the VideoWriter object
out.release()
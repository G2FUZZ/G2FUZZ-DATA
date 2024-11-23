# Import necessary libraries
import numpy as np
import cv2

# Define the video codec to be used
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'h264' or 'h265' for other codecs

# Specify the output file path
output_file = './tmp/extended_video.mp4'

# Define the resolution and frame rate
width = 640
height = 480
fps = 30

# Create a VideoWriter object to write the video
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate a more complex video with rotating rectangle and changing colors
for i in range(100):
    img = np.ones((height, width, 3), np.uint8) * 255  # White background
    angle = i * 3  # Rotate rectangle gradually
    color = (i * 2 % 256, (i * 5) % 256, (i * 10) % 256)  # Change color for each frame
    cv2.rectangle(img, (200, 200), (400, 300), color, -1)  # Draw a filled rectangle
    M = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)  # Rotation matrix
    img = cv2.warpAffine(img, M, (width, height))  # Apply rotation
    text = f'Frame: {i}'
    cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    out.write(img)

# Release the VideoWriter object and close the file
out.release()
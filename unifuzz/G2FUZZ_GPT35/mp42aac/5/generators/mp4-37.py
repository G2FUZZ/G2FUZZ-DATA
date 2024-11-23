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

# Generate a more complex video with multiple shapes, animated gradients, and text animations
for i in range(100):
    img = np.zeros((height, width, 3), np.uint8)  # Black background
    for j in range(10):
        color = (i * 5 % 256, (i * 10) % 256, (i * 15) % 256)  # Change color for each frame
        cv2.rectangle(img, (j*50, j*50), (width - j*50, height - j*50), color, -1)  # Draw filled rectangles with gradient colors
    angle = i * 3  # Rotate shapes gradually
    M = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)  # Rotation matrix
    img = cv2.warpAffine(img, M, (width, height))  # Apply rotation
    radius = 50 + i % 50  # Change radius of the circle
    opacity = 150 + i % 100  # Change opacity of the circle
    cv2.circle(img, (width // 2, height // 2), radius, (255, 255, 255), -1, lineType=cv2.LINE_AA, shift=0)  # Draw a filled circle
    cv2.addWeighted(img, 0.5, cv2.circle(img.copy(), (width // 2, height // 2), radius, (0, 0, 255), -1), 0.5, 0, img)  # Blend two images
    text = f'Frame: {i}'
    cv2.putText(img, text, (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    out.write(img)

# Release the VideoWriter object and close the file
out.release()
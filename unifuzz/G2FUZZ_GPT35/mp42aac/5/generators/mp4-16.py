# Import necessary libraries
import numpy as np
import cv2

# Define the video codec to be used
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'h264' or 'h265' for other codecs

# Specify the output file path
output_file = './tmp/generated_video_with_user_data.mp4'

# Define the resolution and frame rate
width = 640
height = 480
fps = 30

# Create a VideoWriter object to write the video
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Generate a simple color gradient video
for i in range(100):
    img = np.ones((height, width, 3), np.uint8) * i
    out.write(img)

# Add User Data to the video file
user_data = 'Custom User Data: This is some custom information stored in the User Data field of the mp4 file.'
with open(output_file, 'a') as file:
    file.write(user_data)

# Release the VideoWriter object and close the file
out.release()
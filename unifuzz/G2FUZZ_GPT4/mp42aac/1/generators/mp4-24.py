import numpy as np
import cv2
import os
from mutagen.mp4 import MP4, MP4Cover

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video specifications
output_filename = output_dir + "example_streaming_with_aux.mp4"
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

# Create a cover image dynamically
cover_img_path = './tmp/cover.jpg'
cover_img = np.zeros((300, 300, 3), dtype=np.uint8)  # Create a black image for cover
cover_img = cv2.putText(cover_img, 'Cover', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imwrite(cover_img_path, cover_img)

# Adding Auxiliary Information (e.g., cover image) after video creation
file = MP4(output_filename)

# Load the dynamically created cover image
with open(cover_img_path, 'rb') as img:
    file["covr"] = [
        MP4Cover(img.read(), imageformat=MP4Cover.FORMAT_JPEG)
    ]

file.save()

print(f"Video with auxiliary information successfully saved to {output_filename}")
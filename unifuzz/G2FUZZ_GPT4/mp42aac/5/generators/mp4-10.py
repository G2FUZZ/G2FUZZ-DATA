import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
text = "Efficiency: MP4 files are designed to be highly efficient in terms of compression, enabling the storage and transmission of high-quality video and audio with relatively small file sizes."

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 files
output_file = os.path.join(output_dir, 'efficiency.mp4')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Prepare text overlay
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)
font_thickness = 2
x, y = 50, 50  # Text start position
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_w, text_h = text_size

# Calculate number of frames
total_frames = fps * duration

# Generate frames
for frame in range(total_frames):
    # Create a blank image
    img = np.zeros((height, width, 3), np.uint8)
    
    # Add text
    cv2.putText(img, text, (x, y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)
    
    # Write the frame to the video file
    out.write(img)

# Release the VideoWriter object
out.release()

print(f"Video file saved: {output_file}")
import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output path for the mp4 file
output_file_path = os.path.join(output_dir, 'compatibility.mp4')

# Define the video specifications
frame_width = 640
frame_height = 480
fps = 24
duration_seconds = 5
total_frames = duration_seconds * fps

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec
out = cv2.VideoWriter(output_file_path, fourcc, fps, (frame_width, frame_height))

# Generate frames and add text
for frame_num in range(total_frames):
    # Create a blank image
    img = np.zeros((frame_height, frame_width, 3), np.uint8)
    img.fill(255) # make the frame white
    
    # Define text properties
    text = "Compatibility: Designed to be compatible with a wide range of devices."
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_color = (0, 0, 0) # black
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    
    # Calculate text position (to be at the center)
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = (img.shape[0] + text_size[1]) // 2
    
    # Put the text on the frame
    cv2.putText(img, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    # Write the frame to the video
    out.write(img)

# Release the VideoWriter object
out.release()

print(f"Video saved to {output_file_path}")
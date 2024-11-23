import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the video
width, height = 640, 480
fps = 24
duration_sec = 5
background_color = (255, 255, 255)  # White background

# Prepare text to display in the video
text = "Compatibility: MP4 files are widely supported by various devices and platforms, " \
       "including smartphones, tablets, PCs, and smart TVs, ensuring that content is accessible " \
       "to a broad audience."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # Black text
thickness = 2
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2

# Prepare the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the video
video_filename = os.path.join(output_dir, "compatibility.mp4")
out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

for _ in range(fps * duration_sec):
    # Create a blank image with the background color
    frame = np.full((height, width, 3), background_color, np.uint8)
    
    # Put the text in the frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    # Write the frame to the video
    out.write(frame)

# Release the video writer
out.release()

print(f"Video saved as {video_filename}")
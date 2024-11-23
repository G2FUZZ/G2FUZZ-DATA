import cv2
import numpy as np

# Set parameters for the video
width, height = 640, 360
fps = 24
duration = 5  # seconds
background_color = (255, 255, 255)

# Text settings
text_content = "10. **Compatibility**: They are widely compatible with media players, web browsers, and devices, making them a universal format for distributing and accessing multimedia content."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_color = (0, 0, 0)
font_thickness = 2

# Calculate text size to center the text
text_size = cv2.getTextSize(text_content, font, font_scale, font_thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2

# Create a blank image/frame
frame = np.full((height, width, 3), background_color, np.uint8)

# Put the text onto the frame
cv2.putText(frame, text_content, (text_x, text_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
output_path = './tmp/compatibility.mp4'
video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Write the same frame for the entire duration of the video
for _ in range(fps * duration):
    video.write(frame)

# Release everything when job is finished
video.release()
cv2.destroyAllWindows()
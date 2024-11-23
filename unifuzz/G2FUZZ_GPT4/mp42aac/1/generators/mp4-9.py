import cv2
import numpy as np
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a simple video with OpenCV
fps = 24
duration = 5  # seconds
frame_size = (640, 480)

# Create a black image
img = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
out = cv2.VideoWriter('./tmp/output_with_sub_and_obj_desc.mp4', fourcc, fps, frame_size)

# Define text properties
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello, World!"
text_size = cv2.getTextSize(text, font, 1, 2)[0]
text_x = (frame_size[0] - text_size[0]) // 2
text_y = frame_size[1] - 50
color = (255, 255, 255)

# Assume we are including an object descriptor for an interactive button
# In a real implementation, this might involve metadata standards not directly supported by OpenCV.
# For demonstration, we'll simulate this visually.
button_text = "Click Me"
button_position = (50, 50)  # Top-left corner of the button
button_size = cv2.getTextSize(button_text, font, 1, 2)[0]
button_end = (button_position[0] + button_size[0] + 20, button_position[1] + button_size[1] + 10)  # Padding for button
button_color = (0, 255, 0)

for _ in range(fps * duration):
    frame = img.copy()
    # Put the text on each frame
    cv2.putText(frame, text, (text_x, text_y), font, 1, color, 2, cv2.LINE_AA)
    # Draw a rectangle and put text to simulate an interactive button
    cv2.rectangle(frame, button_position, button_end, button_color, 2)
    cv2.putText(frame, button_text, (button_position[0] + 10, button_end[1] - 5), font, 1, button_color, 2, cv2.LINE_AA)
    out.write(frame)

# Release everything if job is finished
out.release()

print("MP4 file with subtitles and simulated object descriptors has been generated and saved to ./tmp/output_with_sub_and_obj_desc.mp4")
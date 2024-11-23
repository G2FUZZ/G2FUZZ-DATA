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
out = cv2.VideoWriter('./tmp/output_with_sub.mp4', fourcc, fps, frame_size)

# Define text properties
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello, World!"
text_size = cv2.getTextSize(text, font, 1, 2)[0]
text_x = (frame_size[0] - text_size[0]) // 2
text_y = frame_size[1] - 50
color = (255, 255, 255)

for _ in range(fps * duration):
    frame = img.copy()
    # Put the text on each frame
    cv2.putText(frame, text, (text_x, text_y), font, 1, color, 2, cv2.LINE_AA)
    out.write(frame)

# Release everything if job is finished
out.release()

print("MP4 file with subtitles has been generated and saved to ./tmp/output_with_sub.mp4")
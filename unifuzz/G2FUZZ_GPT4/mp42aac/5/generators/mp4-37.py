import cv2
import numpy as np
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the video
width, height = 640, 480
fps = 24
duration = 10  # seconds
output_filename = os.path.join(output_dir, f"complex_example_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4")

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 files
video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Generate frames and write to the file
for t in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Background fade from black to blue
    fade_color = min(255, int((255/duration) * (t/fps)))
    frame[:, :] = (fade_color, fade_color, 255)  # Blueish background
    
    # Animated square
    size = 50
    x = int((width - size) * (t / (fps * duration)))
    y = height // 2 - size // 2
    frame[y:y+size, x:x+size] = (0, 255, 0)  # Green square
    
    # Animated text
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Time: {t//fps}s"
    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    textX = (frame.shape[1] - textsize[0]) // 2
    textY = (frame.shape[0] + textsize[1]) // 2
    cv2.putText(frame, text, (textX, textY), font, 1, (255, 255, 255), 2)
    
    # Additional animation: Circle moving vertically
    circle_radius = 20
    circle_x = width - 60  # Fixed X position
    circle_y = int((height - circle_radius) * (t / (fps * duration)))
    cv2.circle(frame, (circle_x, circle_y), circle_radius, (255, 0, 0), -1)  # Blue circle

    video.write(frame)

# Release the video writer
video.release()

print(f"Video saved as {output_filename}")
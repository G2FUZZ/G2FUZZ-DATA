import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output path
output_path = os.path.join(output_dir, "example_streaming.mp4")

# Video properties
width, height = 640, 360
fps = 24
duration_sec = 5
background_color = (255, 0, 0)  # Red background
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Streaming Video"
font_scale = 1
font_color = (255, 255, 255)  # White text
text_thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, text_thickness)
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Generate each frame
for _ in range(fps * duration_sec):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:] = background_color
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, text_thickness)
    video_writer.write(frame)

# Release the video writer
video_writer.release()

print(f"Video saved to {output_path}")
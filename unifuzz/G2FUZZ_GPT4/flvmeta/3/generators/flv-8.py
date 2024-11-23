import os
import cv2
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the text to be added to the video
text = """
8. Compatibility: Despite the decline in usage due to the rise of HTML5 video and newer, more efficient formats like MP4, FLV files are still compatible with many standalone media players, video editing software, and some web browsers with the appropriate plugins.
"""

# Define basic parameters for the video
width, height = 640, 480
fps = 24
duration = 5  # seconds
font_scale = 1.0
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# Calculate the number of frames
num_frames = duration * fps

# Create a blank image to calculate text size
(text_width, text_height), _ = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)
x = (width - text_width) // 2
y = (height - text_height) // 2

# OpenCV doesn't directly support FLV, so we use XVID codec and later convert the file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
temp_video_path = './tmp/output.avi'
flv_video_path = './tmp/output.flv'

# Create a VideoWriter object
out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

for _ in range(num_frames):
    frame = np.full((height, width, 3), background_color, np.uint8)
    cv2.putText(frame, text, (x, y), font, font_scale, text_color, 1, cv2.LINE_AA)
    out.write(frame)

# Release the VideoWriter
out.release()

# Convert the AVI video to FLV using FFmpeg
os.system(f"ffmpeg -i {temp_video_path} -c:v flv -f flv {flv_video_path}")

# Optionally, delete the temporary AVI file
os.remove(temp_video_path)
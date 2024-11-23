import os
import cv2
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the text to be added to the video with an additional feature
text = """
8. Compatibility: Despite the decline in usage due to the rise of HTML5 video and newer, more efficient formats like MP4, FLV files are still compatible with many standalone media players, video editing software, and some web browsers with the appropriate plugins.
9. **Tagging System**: The FLV file structure includes a flexible tagging system for video, audio, and metadata. This system allows for the addition of future data types and encoding formats without significantly altering the core file structure, providing a level of future-proofing.
"""

# Define basic parameters for the video
width, height = 640, 480
fps = 24
duration = 10  # Adjusted duration to fit additional text
font_scale = 1.0
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# Calculate the number of frames
num_frames = duration * fps

# Create a blank image to calculate text size
(text_width, text_height), _ = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)
x = (width - text_width) // 2
# Adjust initial y to start drawing text from top to fit all content
y_start = 20
line_height = text_height + 10  # Adjust based on font size

# OpenCV doesn't directly support FLV, so we use XVID codec and later convert the file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
temp_video_path = './tmp/output_with_tags.avi'
flv_video_path = './tmp/output_with_tags.flv'

# Create a VideoWriter object
out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

for _ in range(num_frames):
    frame = np.full((height, width, 3), background_color, np.uint8)
    y = y_start
    for line in text.split('\n'):
        # Check and adjust y position for each line to ensure it fits in the frame
        if y + line_height > height:
            break  # Avoid drawing text outside the frame
        cv2.putText(frame, line.strip(), (x, y), font, font_scale, text_color, 1, cv2.LINE_AA)
        y += line_height  # Move to the next line
    out.write(frame)

# Release the VideoWriter
out.release()

# Convert the AVI video to FLV using FFmpeg
os.system(f"ffmpeg -i {temp_video_path} -c:v flv -f flv {flv_video_path}")

# Optionally, delete the temporary AVI file
os.remove(temp_video_path)
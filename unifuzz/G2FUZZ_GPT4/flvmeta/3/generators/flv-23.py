import os
import cv2
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the text to be added to the video
text = """
8. Compatibility: Despite the decline in usage due to the rise of HTML5 video and newer, more efficient formats like MP4, FLV files are still compatible with many standalone media players, video editing software, and some web browsers with the appropriate plugins.
"""

# Additional metadata for injection
metadata_text = """
3. **Metadata Injection**: FLV files allow for the injection of additional metadata after the file has been created. Tools and software are available that can add or modify metadata such as duration, width, height, and custom key-value pairs, aiding in content management and delivery optimization.
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
metadata_injected_flv_path = './tmp/output_with_metadata.flv'

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

# Inject metadata into the FLV file
metadata_command = f"ffmpeg -i {flv_video_path} -metadata title='Sample Video' -metadata comment='{metadata_text}' {metadata_injected_flv_path}"
os.system(metadata_command)

# Optionally, delete the temporary AVI file and original FLV file without metadata
os.remove(temp_video_path)
os.remove(flv_video_path)
import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
video_file_path = os.path.join(output_dir, 'output_fragmented_mpeg4.mp4')

# Define the codec for MPEG-4 Part 2 (may require 'DIVX', 'XVID' or 'FMP4' depending on your system)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 'XVID' is often used for MPEG-4 Part 2

# Create VideoWriter object with additional argument for fMP4
# Note: To enable fragmented MP4, we specify an extra flag `cv2.VIDEOWRITER_PROP_IS_COLOR` with `True`
# This does not directly relate to fMP4, but it's necessary to set properties for VideoWriter in some cases
out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height), isColor=True)

# In OpenCV, direct support for writing fragmented MP4 files is not clearly documented or may not be fully supported.
# The code below continues as usual but for actual fMP4 support, consider using a post-processing step with ffmpeg or a similar tool:
# Example ffmpeg command to convert to fMP4: `ffmpeg -i input.mp4 -movflags faststart+frag_keyframe+empty_moov output_fmp4.mp4`
# This command re-encodes the video to be fragmented.

# Generate frames
for i in range(fps * duration):
    # Create a blank image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Add some text to the frame
    cv2.putText(frame, f'Frame {i+1}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Write the frame into the file
    out.write(frame)

# Release everything when the job is finished
out.release()
print(f'Video saved to {video_file_path}')

# Reminder: For true fMP4 support, consider using ffmpeg for post-processing.
# This code as-is will produce a standard MP4 file. See the commented ffmpeg command for converting to fMP4.
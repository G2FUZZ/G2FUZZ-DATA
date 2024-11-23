import cv2
import numpy as np
import os

# Ensure tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video settings
width, height = 640, 480
fps = 24
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
video_filename = './tmp/sample_video_with_tool_extensions.mp4'

# Additional settings for low latency streaming and tool extensions
parameters = [
    (cv2.VIDEOWRITER_PROP_QUALITY, 95),  # High quality setting, assuming lower compression, faster encoding
    # Assuming 'TOOL_EXTENSIONS' is a hypothetical parameter to enable tool extensions in the output video.
    # Note: OpenCV does not directly support a parameter to enable tool extensions as described.
    # This line is illustrative and would need to be replaced or implemented with actual tool extension enabling methods.
    # ('TOOL_EXTENSIONS', 1),  # Enabling tool extensions
]

# Create VideoWriter object with additional parameters
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))
for param, value in parameters:
    out.set(param, value)

# Generate video content (A simple animation of a moving white square on a black background)
num_frames = 120  # 5 seconds of video at 24 fps
for i in range(num_frames):
    frame = np.zeros((height, width, 3), np.uint8)  # Black background
    cv2.rectangle(frame, (10 + i*5, 50), (60 + i*5, 100), (255, 255, 255), -1)  # Moving white square
    out.write(frame)

# Release everything when job is finished
out.release()
cv2.destroyAllWindows()
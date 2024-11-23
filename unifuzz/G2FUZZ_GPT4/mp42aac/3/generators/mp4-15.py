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
video_filename = './tmp/sample_video_low_latency.mp4'

# Additional settings for low latency streaming
# Note: While OpenCV does not directly support creating videos optimized for low latency streaming,
# it's important to choose the right codec and settings that can be compatible with further processing
# for low latency streaming. The actual optimization for low latency will need to be performed
# with additional tools or during the streaming process itself.
parameters = [
    (cv2.VIDEOWRITER_PROP_QUALITY, 95),  # High quality setting, assuming lower compression, faster encoding
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
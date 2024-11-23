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
video_filename = './tmp/sample_video.mp4'

# Create VideoWriter object
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))

# Generate video content (A simple animation of a moving white square on a black background)
num_frames = 120  # 5 seconds of video at 24 fps
for i in range(num_frames):
    frame = np.zeros((height, width, 3), np.uint8)  # Black background
    cv2.rectangle(frame, (10 + i*5, 50), (60 + i*5, 100), (255, 255, 255), -1)  # Moving white square
    out.write(frame)

# Release everything when job is finished
out.release()
cv2.destroyAllWindows()
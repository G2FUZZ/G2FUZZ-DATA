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
video_filename = './tmp/sample_video_low_latency_with_scalability.mp4'

# Additional settings for low latency streaming
parameters = [
    (cv2.VIDEOWRITER_PROP_QUALITY, 95),  # High quality setting
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

# Note: OpenCV itself does not support direct creation of videos with temporal and spatial scalability (SVC).
# This requires post-processing with tools capable of re-encoding the video to an SVC-compatible format.
# The following is a conceptual representation of how you might prepare your video for SVC with external tools:

# 1. Use ffmpeg or another tool to encode the video with scalability options.
# Example using ffmpeg (this is a hypothetical example, adjust parameters as needed):
# os.system(f"ffmpeg -i {video_filename} -c:v libx264 -preset veryslow -profile:v high -level 4.0 -x264-params 'ref=4:bframes=3:b_adapt=2:direct=auto:me=umh:subme=8:merange=24' -maxrate 1000k -bufsize 2000k -vf 'scale=-2:720,format=yuv420p' -flags +cgop -g 30 -dash 1 {video_filename.replace('.mp4', '_svc.mp4')}")

# Remember, for actual deployment, replace the os.system call with subprocess.call or similar to handle shell execution more securely.
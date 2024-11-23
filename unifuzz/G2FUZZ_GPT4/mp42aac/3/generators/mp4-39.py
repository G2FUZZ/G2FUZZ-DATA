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

# Additional settings for low latency streaming and high quality
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

# Code to handle Codec Configuration Boxes (example with H.264 video codec)
# This is done during the encoding process, where specific codec information is added to the video file.
# The following example uses ffmpeg for encoding the video with H.264 codec and includes the Codec Configuration Boxes automatically.

# Note: OpenCV itself does not support direct insertion of Codec Configuration Boxes.
# This step is usually handled by video encoders like ffmpeg during the video encoding process.
# The AVC (H.264) Codec Configuration Box (avcC) will be included in the MP4 file when encoded with libx264 codec.
encrypted_video_filename = video_filename.replace('.mp4', '_encrypted_with_avcc.mp4')
os.system(f"""
ffmpeg -i {video_filename} -c:v libx264 -preset veryslow -profile:v high -level 4.0 \
-x264-params 'ref=4:bframes=3:b_adapt=2:direct=auto:me=umh:subme=8:merange=24' \
-maxrate 1000k -bufsize 2000k -vf 'scale=-2:720,format=yuv420p' -flags +cgop -g 30 -dash 1 -movflags frag_keyframe+empty_moov \
-c:a copy -tag:v encv -encryption_scheme cenc-aes-ctr -encryption_key 76a6c65c5ea762046bd749a2e632ccbb \
-encryption_kid 303132333435363738393a3b3c3d3e3f {encrypted_video_filename}
""")

# Remember, for actual deployment, replace the os.system call with subprocess.call or similar to handle shell execution more securely.
# The encryption_key and encryption_kid are just examples, and they should be replaced with your actual encryption key and key ID.
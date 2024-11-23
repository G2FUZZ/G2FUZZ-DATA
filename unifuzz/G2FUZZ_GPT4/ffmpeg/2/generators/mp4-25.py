import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# Video properties
width, height = 640, 480
fps = 24
duration_sec = 5
frame_count = fps * duration_sec

# Setup output video path and codec
output_path = os.path.join(output_dir, 'avc_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # 'avc1' is the codec for H.264

# Create a video writer object
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

for i in range(frame_count):
    # Create a frame with a solid color that changes over time
    # Colors are in BGR format
    frame = np.zeros((height, width, 3), np.uint8)
    color_value = i % 255  # Cycle through color values
    frame[:] = [color_value, color_value, color_value]
    
    # Write the frame to the video file
    out.write(frame)

# Release the video writer
out.release()

# To add hint tracks for streaming, we unfortunately cannot utilize OpenCV directly.
# Instead, we will use the `VideoFileClip` from moviepy to read and then write the video,
# which does not inherently add hint tracks, but we can use ffmpeg (which moviepy uses under the hood)
# as a workaround to add hint tracks post-creation.

# The path for the video with hint tracks
hinted_video_path = os.path.join(output_dir, 'avc_video_hinted.mp4')

# Use ffmpeg command line (through os.system) to add hint tracks for streaming
# This requires ffmpeg to be installed on your system
ffmpeg_cmd = f"ffmpeg -i {output_path} -c copy -movflags +faststart+rtphint {hinted_video_path}"
os.system(ffmpeg_cmd)

print(f"Video file with hint tracks saved at: {hinted_video_path}")
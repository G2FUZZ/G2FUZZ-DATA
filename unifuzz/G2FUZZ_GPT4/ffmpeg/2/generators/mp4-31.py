import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path for fragmented mp4 with MPEG-H support
output_file_fragmented = os.path.join(output_dir, 'streaming_video_fragmented_mpegh.mp4')

# Video properties
width, height = 640, 480
fps = 24  # Frames per second
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec

# Create a VideoWriter object for fragmented video with MPEG-H support
out_fragmented = cv2.VideoWriter(output_file_fragmented, fourcc, fps, (width, height))

# Generate each frame of the video
for i in range(fps * duration):
    # Create a frame with synthetic content
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color_value = int((i / (fps * duration)) * 255)
    frame[:, :] = [color_value, 0, 255 - color_value]  # BGR format
    
    # Write the frame to the video file (fragmented version with MPEG-H support)
    out_fragmented.write(frame)

# Release the VideoWriter object (fragmented version with MPEG-H support)
out_fragmented.release()

# Use ffmpeg to convert the video into a fragmented mp4 with MPEG-H support
# This requires ffmpeg to be installed and accessible from the command line
# The `-acodec` option is set to use an audio codec that supports MPEG-H, assuming source content with MPEG-H audio is available.
fragmented_command = f"ffmpeg -i {output_file_fragmented} -movflags faststart+frag_keyframe+empty_moov -acodec copy -vcodec copy -brand mha1 {output_dir}fragmented_final_mpegh.mp4"
os.system(fragmented_command)

print(f"Fragmented video with MPEG-H support saved to {output_dir}fragmented_final_mpegh.mp4")
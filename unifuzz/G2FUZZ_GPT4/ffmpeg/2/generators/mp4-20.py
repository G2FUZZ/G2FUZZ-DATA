import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path for fragmented mp4
output_file_fragmented = os.path.join(output_dir, 'streaming_video_fragmented.mp4')

# Video properties
width, height = 640, 480
fps = 24  # Frames per second
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec

# Create a VideoWriter object for fragmented video
# Note: OpenCV does not directly support video fragmentation. 
# Therefore, we will create the video as usual and then use ffmpeg to post-process it for fragmentation.
out_fragmented = cv2.VideoWriter(output_file_fragmented, fourcc, fps, (width, height))

# Generate each frame of the video
for i in range(fps * duration):
    # Create a frame with synthetic content
    # Here, we use a simple color gradient changing over time
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color_value = int((i / (fps * duration)) * 255)
    frame[:, :] = [color_value, 0, 255 - color_value]  # BGR format
    
    # Write the frame to the video file (fragmented version)
    out_fragmented.write(frame)

# Release the VideoWriter object (fragmented version)
out_fragmented.release()

# Use ffmpeg to convert the video into a fragmented mp4
# This requires ffmpeg to be installed and accessible from the command line
fragmented_command = f"ffmpeg -i {output_file_fragmented} -movflags faststart+frag_keyframe+empty_moov -acodec copy -vcodec copy {output_dir}fragmented_final.mp4"
os.system(fragmented_command)

print(f"Fragmented video saved to {output_dir}fragmented_final.mp4")
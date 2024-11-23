import cv2
import numpy as np
import os
from subprocess import call

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use mp4v for ISO Base Media File Format compatibility
output_filename = os.path.join(output_dir, 'example_isobmff.mp4')

# Create a video writer object
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Generate frames
for i in range(duration * fps):
    # Create a black image
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the square's position to create a moving effect
    center_x = int((width // 2) + (width // 4) * np.sin(2 * np.pi * i / (fps * 2)))
    center_y = int((height // 2) + (height // 4) * np.cos(2 * np.pi * i / (fps * 2)))
    start_point = (center_x - 50, center_y - 50)
    end_point = (center_x + 50, center_y + 50)
    
    # Draw a blue square
    cv2.rectangle(frame, start_point, end_point, (255, 0, 0), -1)
    
    # Write the frame to the video file
    out.write(frame)

# Release the video writer
out.release()

# Convert the video for adaptive streaming
# Generate the DASH (MPEG-DASH) MPD (Media Presentation Description) file for adaptive streaming
mpd_output = os.path.join(output_dir, 'stream.mpd')
ffmpeg_cmd = [
    'ffmpeg',
    '-i', output_filename,
    '-codec:v', 'libx264', '-b:v', '800k',
    '-vf', 'scale=-2:720', '-bf', '1', '-keyint_min', '120', '-g', '120', '-sc_threshold', '0',
    '-b_strategy', '0', '-use_timeline', '1', '-use_template', '1',
    '-adaptation_sets', 'id=0,streams=v id=1,streams=a',
    '-f', 'dash', mpd_output
]

call(ffmpeg_cmd)

print(f"Adaptive Streaming MPD file generated at {mpd_output}")
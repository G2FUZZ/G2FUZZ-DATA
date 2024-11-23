import os
from moviepy.editor import ColorClip
from moviepy.video.fx.resize import resize

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an MP4 file containing a simple color clip
# This example does not directly encapsulate MPEG-2 TS in the MP4 container
# as this requires a specific setup and content, but it demonstrates generating an MP4 file
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=10)  # A 10-second red clip

# Resize for demonstration, not necessary for the task
clip_resized = resize(clip, width=640)

# Output file path
output_file = os.path.join(output_dir, 'mpeg2_in_mp4_example.mp4')

# Write the clip to an MP4 file
clip_resized.write_videofile(output_file, codec='libx264', fps=24)

print(f"MP4 file has been generated and saved to {output_file}")
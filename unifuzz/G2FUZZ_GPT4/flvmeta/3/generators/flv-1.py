import os
from moviepy.editor import ColorClip

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the output file path
output_file = os.path.join(output_dir, "example.flv")

# Create a simple color clip as an example video
# This will be a 5-second red color clip with a resolution of 640x480
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Set FPS
clip.fps = 24

# Write the video file in FLV format
clip.write_videofile(output_file, codec="flv")

# Release resources
clip.close()
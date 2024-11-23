import os
from moviepy.editor import ColorClip

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a simple color clip, as an example content for the FLV file
# This is a 5-second red color clip, with a resolution of 640x480
color_clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# FLV file path
flv_path = os.path.join(output_dir, "example_video.flv")

# Generate the FLV file directly
color_clip.write_videofile(flv_path, codec="flv", fps=24)

print(f"FLV file has been created at: {flv_path}")
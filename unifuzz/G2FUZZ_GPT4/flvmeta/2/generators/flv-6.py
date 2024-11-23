import os
from moviepy.editor import ColorClip

# Create the tmp/ directory if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the output FLV file
flv_file_path = os.path.join(output_dir, "sample.flv")

# Create a simple color clip, here a 5-second red clip in 640x480.
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Write the clip to a .flv file
clip.write_videofile(flv_file_path, codec="libx264", fps=24, audio=False)
import os
from moviepy.editor import ColorClip

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the FLV file properties
flv_filename = os.path.join(output_dir, "sample.flv")
duration = 1  # Duration in seconds
width = 320  # Width of the video
height = 240  # Height of the video
color = (255, 0, 0)  # Red

# Create a simple color clip
clip = ColorClip(size=(width, height), color=color, duration=duration)

# Write the video file in FLV format without the 'format' argument
clip.write_videofile(flv_filename, codec="libx264", fps=24, audio=False, preset="ultrafast")

print(f"FLV file has been generated: {flv_filename}")
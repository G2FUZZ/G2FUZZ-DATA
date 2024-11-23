from moviepy.editor import ColorClip
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the clip
duration = 1  # Duration in seconds
resolution = (640, 480)  # Resolution of the clip
color = (255, 0, 0)  # Color of the clip (Red in this case)

# Creating a color clip
clip = ColorClip(size=resolution, color=color, duration=duration)

# Setting the file name for the FLV file
flv_file_name = os.path.join(output_dir, "example.flv")

# Exporting the clip as an FLV file
clip.write_videofile(flv_file_name, codec="libx264", fps=24)
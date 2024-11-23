import os
from moviepy.editor import ColorClip

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the video
duration = 5  # duration of the video in seconds
resolution = (640, 360)  # resolution of the video
color = (255, 0, 0)  # color of the video in RGB

# Create a color clip
clip = ColorClip(size=resolution, color=color, duration=duration)

# Export the clip as an FLV file, specifying the fps
flv_filename = os.path.join(output_dir, 'streaming_capability.flv')
clip.write_videofile(flv_filename, codec='flv', fps=24)  # Added fps=24 here

print(f"FLV file with streaming capabilities has been saved to {flv_filename}")
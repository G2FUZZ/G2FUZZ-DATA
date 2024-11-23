from moviepy.editor import ColorClip
import os

# Directory to save the FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# FLV file properties
duration = 10  # seconds
width = 640
height = 360
fps = 24  # Frame per second

# Create a color clip as a sample video
clip = ColorClip(size=(width, height), color=(255, 0, 0), duration=duration).set_fps(fps)

# Specify the file path
file_path = os.path.join(output_dir, 'sample.flv')

# Write the video file with metadata
clip.write_videofile(file_path, codec='flv', fps=fps)

print(f"FLV file has been saved to {file_path}")
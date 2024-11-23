from moviepy.editor import ColorClip
from moviepy.video.fx import resize
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, 'sample.flv')

# Generate a simple video clip (e.g., a 5-second red screen)
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=5)

# Optional: Resize the clip if needed
# clip = clip.fx(resize, width=640) # Example of resizing, modify as needed

# Write the video file with the H.264 codec within an FLV container
clip.write_videofile(output_file, codec='libx264', fps=24)
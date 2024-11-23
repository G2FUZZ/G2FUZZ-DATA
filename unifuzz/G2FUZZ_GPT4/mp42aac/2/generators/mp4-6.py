from moviepy.editor import ColorClip
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple video clip
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=10)  # A 10-second red video

# Set the output file path
output_file = os.path.join(output_dir, 'example.mp4')

# Write the video file to disk
clip.write_videofile(output_file, codec="libx264", fps=24)

print(f"Video saved to {output_file}")
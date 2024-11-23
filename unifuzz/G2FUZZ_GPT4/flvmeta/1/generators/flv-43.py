from moviepy.editor import ColorClip
import subprocess
import os

# Define the properties of the clip
duration = 10  # Duration in seconds
width = 640  # Width of the clip
height = 360  # Height of the clip
fps = 24  # Frames per second
video_bitrate = "2000k"  # Video bitrate

# Create a temporary color clip
color_clip = ColorClip(size=(width, height), color=(255, 0, 0), duration=duration)
color_clip = color_clip.set_fps(fps)

# Define the output path for the temporary mp4 file and the final flv file
tmp_mp4_path = './tmp/temp_clip.mp4'
final_flv_path = './tmp/final_clip.flv'

# Ensure the tmp directory exists
os.makedirs(os.path.dirname(tmp_mp4_path), exist_ok=True)

# Write the color clip to a temporary mp4 file
color_clip.write_videofile(tmp_mp4_path, codec="libx264", bitrate=video_bitrate)

# Convert the mp4 file to flv format using ffmpeg command line with additional flags for quality control and metadata
subprocess.run([
    'ffmpeg', '-i', tmp_mp4_path, 
    '-f', 'flv', 
    '-vb', video_bitrate, 
    '-metadata', 'title=Example Title', 
    '-metadata', 'author=Example Author', 
    final_flv_path])

# Clean up the temporary mp4 file
os.remove(tmp_mp4_path)

print(f"FLV file has been saved to {final_flv_path}")
from moviepy.editor import ColorClip
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the video
duration = 10  # in seconds
size = (1920, 1080)  # resolution
color = (255, 0, 0)  # red color

# Create a color clip
clip = ColorClip(size=size, color=color, duration=duration)

# Specify the output filename
output_filename = os.path.join(output_dir, "streaming_support_video.mp4")

# Write the video file with codec 'libx264' for MP4 format,
# preset 'fast' to optimize encoding speed, and specify the fps
clip.write_videofile(output_filename, codec="libx264", preset="fast", fps=24)

# Use ffmpeg to optimize the MP4 for streaming (fast start)
# This moves the moov atom to the beginning of the file.
os.system(f"ffmpeg -i {output_filename} -movflags +faststart -codec copy {output_dir}streaming_optimized_video.mp4")
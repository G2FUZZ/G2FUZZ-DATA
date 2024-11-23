from moviepy.editor import ColorClip
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define video properties
video_duration = 10  # seconds
video_size = (1920, 1080)  # resolution
video_fps = 24  # frames per second
video_color = (255, 0, 0)  # red
output_path = './tmp/basic_video.mp4'

# Create a basic color clip
clip = ColorClip(size=video_size, color=video_color, duration=video_duration).set_fps(video_fps)

# Write the video file to disk
clip.write_videofile(output_path, codec="libx264", fps=video_fps)

print(f"Generated MP4 video at {output_path}")
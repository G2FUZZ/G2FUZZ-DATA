from moviepy.editor import ColorClip
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the clip
clip_duration = 5  # duration of the clip in seconds
clip_size = (640, 480)  # size of the clip in pixels
clip_fps = 24  # frames per second
clip_color = (255, 0, 0)  # red color clip

# Create a color clip (you can change the color to anything you like)
clip = ColorClip(size=clip_size, color=clip_color, duration=clip_duration)

# Set the fps
clip = clip.set_fps(clip_fps)

# Export the clip as an FLV file
clip.write_videofile(f"{output_dir}generated_video.flv", codec="flv")
from moviepy.editor import ColorClip
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the properties of the video
video_duration = 5  # seconds
video_fps = 24  # frames per second
video_resolution = (640, 480)  # width, height in pixels
video_color = (255, 0, 0)  # Red color clip

# Create a color clip (red) of specified duration and resolution
clip = ColorClip(size=video_resolution, col=video_color, duration=video_duration)

# Set the codec to H.264 (MPEG-4 AVC) for FLV format and save the file with specified fps
output_file = os.path.join(output_dir, "example_video.flv")
clip.write_videofile(output_file, codec='libx264', fps=video_fps)
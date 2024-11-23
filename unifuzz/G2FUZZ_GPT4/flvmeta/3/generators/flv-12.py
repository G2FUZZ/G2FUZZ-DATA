import os
from moviepy.editor import ColorClip
# from moviepy.video.io.ffmpeg_tools import ffmpeg_add_cue_points  # This function does not exist

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the output file path
output_file = os.path.join(output_dir, "example_with_cue_points.flv")

# Create a simple color clip as an example video
# This will be a 5-second red color clip with a resolution of 640x480
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Set FPS
clip.fps = 24

# Write the video file in FLV format
clip.write_videofile(output_file, codec="flv")

# Release resources
clip.close()

# Define cue points
cue_points = [
    {"time": 1, "name": "FirstCue", "type": "event"},  # At 1 second
    {"time": 3, "name": "SecondCue", "type": "event"}  # At 3 seconds
]

# The following step cannot be done with MoviePy as initially intended
# You would need to use an external tool or script to add cue points to the video file
# ffmpeg_add_cue_points(output_file, cue_points)
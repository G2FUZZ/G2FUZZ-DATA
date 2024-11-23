from moviepy.editor import ColorClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the duration and size of the clip
duration = 5  # seconds
width, height = 640, 480  # Size of the video

# Create a transparent clip (an RGBA clip where A (alpha) is 0)
clip = ColorClip(size=(width, height), color=(0, 0, 0, 0), duration=duration, ismask=True)

# Optional: Add fade in and fade out effects
clip = fadein(clip, 1)  # 1 second fade-in
clip = fadeout(clip, 1)  # 1 second fade-out

# Set the codec and write the video file
output_file = os.path.join(output_dir, 'alpha_video.mov')  # Changed to .mov format
clip.write_videofile(output_file, codec='qtrle', fps=24)  # Changed codec to 'qtrle'
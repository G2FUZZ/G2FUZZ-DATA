import os
from moviepy.editor import ColorClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.video.fx.all import even_size, fadein, fadeout
from moviepy.audio.fx.all import audio_fadein, audio_fadeout
import subprocess

# Specify the path to the ImageMagick binary
# Adjust the path according to your ImageMagick installation
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.11-Q16\magick.exe"  # Example for Windows
# os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"  # Example for Linux/macOS

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Your existing code for creating and processing video clips
# ...

# Make sure to replace the placeholder paths and filenames with actual values suitable for your project
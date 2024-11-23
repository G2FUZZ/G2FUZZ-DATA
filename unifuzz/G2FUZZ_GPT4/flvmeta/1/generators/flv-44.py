import os
from moviepy.editor import concatenate_videoclips, ColorClip, TextClip, CompositeVideoClip
import moviepy.config_defaults as cf

# Specify the path to the ImageMagick binary here
# For Windows, replace the path below with the actual path to your ImageMagick installation
# For macOS/Linux, it might just be 'convert' or 'magick' if already in PATH
cf.IMAGEMAGICK_BINARY = r"C:\Path\To\ImageMagick\magick.exe"  # Windows example
# cf.IMAGEMAGICK_BINARY = "/usr/local/bin/magick"  # macOS/Linux example

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Your existing code continues here...
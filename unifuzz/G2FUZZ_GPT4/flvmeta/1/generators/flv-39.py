from moviepy.editor import VideoFileClip, concatenate_videoclips, VideoClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings
import os
import numpy as np
import json

# Correct way to specify the ImageMagick binary path in MoviePy
# For Windows, replace 'YOUR_PATH_TO_MAGICK' with the path to the 'magick' executable.
# Example: r"C:\Program Files\ImageMagick-7.0.11-Q16-HDRI\magick.exe"
# For Linux/Mac, it's typically not needed if 'convert' is available globally.
change_settings({"IMAGEMAGICK_BINARY": r"YOUR_PATH_TO_MAGICK"})

# Make output directory
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# The rest of your script remains the same...
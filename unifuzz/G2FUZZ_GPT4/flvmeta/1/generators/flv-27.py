from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, TextClip
from moviepy.config import change_settings
import numpy as np
import os
from scipy.io import wavfile

# Directly specify the path to the ImageMagick binary
# Windows example: r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"
# macOS/Linux example: "/usr/local/bin/magick" or "/usr/local/bin/convert"
change_settings({"IMAGEMAGICK_BINARY": r"PATH_TO_IMAGEMAGICK"})

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Rest of your code remains the same...
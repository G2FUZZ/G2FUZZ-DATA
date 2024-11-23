from moviepy.config import change_settings

# Update this path to the actual location of the ImageMagick binary on your system
# For Windows, it might look like r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"
# For Linux/Mac, it might be simply "convert" or the full path to the "convert" binary
imagemagick_path = "/path/to/your/imagemagick/binary"

change_settings({"IMAGEMAGICK_BINARY": imagemagick_path})

# Your existing code follows here...
from moviepy.editor import ColorClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import numpy as np
from scipy.io.wavfile import write
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# (Rest of your code here)
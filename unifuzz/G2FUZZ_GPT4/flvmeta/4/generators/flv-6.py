from moviepy.config import change_settings
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Set the path to ImageMagick binary here. Replace "YOUR_PATH" with the actual path.
# Example: C:\\Program Files\\ImageMagick-7.0.10-Q16\\magick.exe
change_settings({"IMAGEMAGICK_BINARY": r"YOUR_PATH_TO_IMAGEMAGICK_BINARY"})

from moviepy.editor import *

# Your code continues from here...
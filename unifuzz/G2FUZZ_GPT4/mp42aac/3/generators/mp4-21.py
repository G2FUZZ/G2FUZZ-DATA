import os
import numpy as np
import wave
from moviepy.editor import AudioFileClip, ColorClip, concatenate_videoclips
from moviepy.video.VideoClip import TextClip

# Set the path to the ImageMagick binary (Windows example)
# Adjust the path as per your ImageMagick installation
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# [The rest of your script goes here, unchanged from your original submission]
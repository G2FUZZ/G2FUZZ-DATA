import os
from moviepy.editor import ColorClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.video.fx.all import even_size, speedx, fadein, fadeout

# Specify the path to the ImageMagick binary
# For Windows, it might look like this (adjust the path as necessary):
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"
# For macOS or Linux, it might be simply 'convert' if ImageMagick is in your PATH, or a full path:
# os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Your existing code for creating and processing video clips
# ...

# Remember to adjust the rest of your script as necessary
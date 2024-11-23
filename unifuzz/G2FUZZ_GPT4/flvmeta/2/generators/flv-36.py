import os
from gtts import gTTS
from moviepy.editor import (AudioFileClip, ColorClip, CompositeAudioClip,
                            CompositeVideoClip, TextClip, concatenate_videoclips)

# Set the path to the ImageMagick binary
# For Windows, it might look something like this:
# os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.11-Q16\magick.exe"
# For Linux or macOS, it might simply be:
# os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"  # or wherever ImageMagick is installed

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Your existing code follows...
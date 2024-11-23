from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Tags
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255,0,0), duration=2)
clip_path = './tmp/sample_video.mp4'
clip.write_videofile(clip_path, fps=24)

# Add metadata to the MP4 file
video = MP4(clip_path)
video.tags = MP4Tags() # Initialize the tags object

# Add some metadata
video["\xa9nam"] = "Sample Video"  # Title
video["\xa9ART"] = "Artist Name"   # Artist
video["\xa9alb"] = "Sample Album"  # Album
video["\xa9day"] = "2023"          # Year
video["\xa9gen"] = "Experimental"  # Genre

# Save the metadata changes
video.save()
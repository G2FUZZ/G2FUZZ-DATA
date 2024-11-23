from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the output video file
output_path = os.path.join(output_dir, 'output_video_360.mp4')

# Create a simple video clip (e.g., 10 seconds of red screen)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)
clip.write_videofile(output_path, codec="libx264", fps=24)

# Add metadata to the MP4 file
video = MP4(output_path)

# Adding metadata
video["\xa9nam"] = "Sample Title"  # Title
video["\xa9ART"] = "Artist Name"  # Artist
video["\xa9alb"] = "Album Name"  # Album
video["trkn"] = [(1, 10)]  # Track number, Total tracks
video["\xa9day"] = "2023"  # Year

# Adding 360-degree video metadata
# Spherical Video RFC format: https://github.com/google/spatial-media/blob/master/docs/spherical-video-rfc.md
video["sv3d"] = b""  # Placeholder for spatial video box, actual metadata needed here for 360-degree
video["proj"] = b""  # Placeholder for projection box, actual metadata needed here for 360-degree

# Adding cover art (you'll need to have a cover.jpg file for this to work, or you can omit this part)
# with open("cover.jpg", "rb") as f:
#     cover_data = f.read()
# video["covr"] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]

video.save()
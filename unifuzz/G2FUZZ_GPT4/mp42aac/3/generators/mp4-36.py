from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, AtomDataType
import requests
import subprocess

# Define metadata
metadata = {
    'title': 'Sample Title',
    'artist': 'Artist Name',
    'album': 'Album Name',
    # Add more metadata fields as needed
}

# Create a temporary video clip (color clip)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Specify the fps (frames per second) when writing the video file
clip.write_videofile("./tmp/sample_video.mp4", codec="libx264", fps=24)

# Fetch cover art image from a URL (example URL used here)
cover_art_url = "https://www.example.com/cover.jpg"
response = requests.get(cover_art_url)
cover_art_data = response.content

# Add metadata to the MP4 file
video = MP4("./tmp/sample_video.mp4")
video["\xa9nam"] = metadata['title']  # Title
video["\xa9ART"] = metadata['artist']  # Artist
video["\xa9alb"] = metadata['album']  # Album

# Adding cover art (use AtomDataType.JPEG or AtomDataType.PNG based on your image)
video["covr"] = [
    MP4Cover(cover_art_data, imageformat=AtomDataType.JPEG)
]

# Save the modified file
video.save()

# Additional step: Add Extended Color Spaces metadata
# This is a simplified example using ffmpeg to modify the video's color space
# Assuming ffmpeg is installed and available in the system's PATH
# The following command modifies the video to use BT.2020 color space as an example
subprocess.run([
    "ffmpeg",
    "-i", "./tmp/sample_video.mp4",
    "-c:v", "libx264",
    "-color_primaries", "bt2020",
    "-color_trc", "smpte2084",  # HDR transfer characteristic
    "-colorspace", "bt2020nc",  # Non-constant luminance
    "-c:a", "copy",  # Copy audio without re-encoding
    "./tmp/sample_video_with_extended_color_spaces.mp4"
])

print("MP4 file with metadata and extended color spaces has been saved.")
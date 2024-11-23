from moviepy.editor import ColorClip, concatenate_videoclips
from mutagen.mp4 import MP4, MP4Cover
from mutagen.mp4 import AtomDataType
import requests

# Define metadata
metadata = {
    'title': 'Sample Title',
    'artist': 'Artist Name',
    'album': 'Album Name',
    # Add more metadata fields as needed
}

# Create temporary video clips (color clips) with different durations to simulate VFR
clip1 = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
clip2 = ColorClip(size=(640, 480), color=(0, 255, 0), duration=3).set_fps(12)  # Lower fps
clip3 = ColorClip(size=(640, 480), color=(0, 0, 255), duration=2).set_fps(48)  # Higher fps

# Concatenate clips to create a single clip with variable frame rate
final_clip = concatenate_videoclips([clip1, clip2, clip3], method="compose")

# Specify the fps (frames per second) when writing the video file
# Here, fps is set to the highest fps used among the clips to ensure smooth playback
final_clip.write_videofile("./tmp/sample_video_vfr.mp4", codec="libx264", fps=48)

# Fetch cover art image from a URL (example URL used here)
cover_art_url = "https://www.example.com/cover.jpg"
response = requests.get(cover_art_url)
cover_art_data = response.content

# Add metadata to the MP4 file
video = MP4("./tmp/sample_video_vfr.mp4")
video["\xa9nam"] = metadata['title']  # Title
video["\xa9ART"] = metadata['artist']  # Artist
video["\xa9alb"] = metadata['album']  # Album

# Adding cover art (use AtomDataType.JPEG or AtomDataType.PNG based on your image)
video["covr"] = [
    MP4Cover(cover_art_data, imageformat=AtomDataType.JPEG)
]

# Save the modified file
video.save()

print("MP4 file with metadata, cover art, and Variable Frame Rate (VFR) has been saved.")
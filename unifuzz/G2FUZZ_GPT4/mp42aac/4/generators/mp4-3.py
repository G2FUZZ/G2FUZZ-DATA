import os
from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)
video_path = os.path.join(output_dir, "example.mp4")
clip.write_videofile(video_path, fps=24)

# Add metadata to the MP4 file
video = MP4(video_path)
video.tags = MP4Tags()  # Initialize the tags if they don't exist

# Standard tags
video["\xa9nam"] = "Sample Video"  # Title
video["\xa9ART"] = "Artist Name"  # Artist
video["\xa9alb"] = "Album Title"  # Album
video["trkn"] = [(1, 10)]  # Track number, total tracks
video["\xa9day"] = "2023"  # Year

# Custom tags can also be added
video["desc"] = "A sample video with red background"  # Description
video["cprt"] = "Copyright Notice"

# Save the metadata
video.save()

print(f"Generated MP4 file with metadata at: {video_path}")
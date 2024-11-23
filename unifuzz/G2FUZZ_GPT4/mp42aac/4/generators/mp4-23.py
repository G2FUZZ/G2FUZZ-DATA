import os
from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)
video_path = os.path.join(output_dir, "example_with_hints.mp4")
clip.write_videofile(video_path, fps=24)

# Add metadata to the MP4 file
video = MP4(video_path)
video.tags = MP4Tags()  # Initialize the tags if they don't exist

# Standard tags
video["\xa9nam"] = "Sample Video with Hint Tracks"  # Title
video["\xa9ART"] = "Artist Name"  # Artist
video["\xa9alb"] = "Album Title"  # Album
video["trkn"] = [(1, 10)]  # Track number, total tracks
video["\xa9day"] = "2023"  # Year

# Custom tags can also be added
video["desc"] = "A sample video with red background and hint tracks"  # Description
video["cprt"] = "Copyright Notice"

# Unfortunately, adding hint tracks directly via the mutagen library or moviepy is not straightforward,
# as these libraries primarily deal with the editing of video/audio tracks and metadata.
# Hint tracks are typically used in the context of streaming and would require manipulation
# at a lower level or with specialized tools designed for stream optimization.

# For demonstration purposes, this code does not directly add a hint track since
# the required functionality exceeds the capabilities of the used libraries.
# Implementing hint tracks usually involves using tools like GPAC's MP4Box in a post-processing step.

print(f"Generated MP4 file with metadata at: {video_path}")
# Note: Remember to use a tool like MP4Box to add hint tracks to this MP4 file for streaming optimization.
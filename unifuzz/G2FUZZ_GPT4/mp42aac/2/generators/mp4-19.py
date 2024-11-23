from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple video clip (for example, a 5-second red screen)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
video_path = os.path.join(output_dir, 'example_video.mp4')
clip.write_videofile(video_path, fps=24)

# Now let's add metadata to our MP4 file
video = MP4(video_path)

# Adding standard metadata
video["\xa9nam"] = "Example Title"  # Title
video["\xa9ART"] = "Artist Name"  # Artist
video["\xa9alb"] = "Album Name"  # Album
video["\xa9day"] = "2023"  # Year
video["\xa9cmt"] = "A sample video with metadata"  # Comment

# Adding Custom Metadata
video["com.apple.iTunes;CustomField"] = "Custom Value"

# Optionally, add cover art (requires an image file)
# with open("path_to_cover_image.jpg", "rb") as img:
#     video["covr"] = [
#         MP4Cover(img.read(), imageformat=MP4Cover.FORMAT_JPEG)
#     ]

# Save the file with metadata
video.save()
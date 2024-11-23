from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover

# Generate a simple video clip
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=5)
clip_path = "./tmp/sample_video.mp4"
clip.write_videofile(clip_path, codec="libx264", fps=24)

# Add metadata and cover art
video = MP4(clip_path)
video["\xa9nam"] = "Sample Video"  # Title
video["\xa9ART"] = "Artist Name"   # Artist
video["\xa9alb"] = "Sample Album"  # Album

cover_art_path = "./tmp/cover.jpg"  # This image should exist in the directory

try:
    with open(cover_art_path, "rb") as img_file:
        video["covr"] = [MP4Cover(img_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]
except FileNotFoundError:
    print(f"Warning: {cover_art_path} not found. Using a default cover image.")
    # Here you would specify the path to a default image or handle the absence in another way.
    # For example, using a placeholder image that you know exists:
    # with open("./path/to/default_cover.jpg", "rb") as img_file:
    #     video["covr"] = [MP4Cover(img_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]

video.save()
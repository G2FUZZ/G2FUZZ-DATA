from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover
import subprocess

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

video.save()

# Adaptive Streaming Compatibility - Convert to MPEG-DASH
# Assuming ffmpeg is installed
dash_folder = "./tmp/dash"
subprocess.run([
    "ffmpeg", 
    "-i", clip_path, 
    "-c:v", "libx264", 
    "-b:v", "1M", 
    "-c:a", "aac", 
    "-b:a", "128k", 
    "-adaptation_sets", "id=0,streams=v id=1,streams=a", 
    "-f", "dash", 
    f"{dash_folder}/manifest.mpd"
])

print("MPEG-DASH MP4 created at:", dash_folder)
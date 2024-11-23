from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# File path for standard MP4
output_file = os.path.join(output_dir, 'sample_video_with_metadata.mp4')

# File path for fragmented MP4
output_file_fragmented = os.path.join(output_dir, 'sample_video_with_metadata_fragmented.mp4')

# Generate a simple video clip (5 seconds of a solid color)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
clip.write_videofile(output_file, codec="libx264", fps=24)

# Add metadata to the MP4 file
video = MP4(output_file)

# Standard metadata fields
video["\xa9nam"] = "Sample Title"  # Title
video["\xa9ART"] = "Artist Name"   # Artist
video["\xa9alb"] = "Album Name"    # Album
video["trkn"] = [(1, 10)]          # Track number, Total tracks

# Save the file with metadata
video.save()

# Generate a fragmented MP4 file
# Note: For the fragmented version, we need to use ffmpeg directly with extra parameters
# `-movflags +frag_keyframe+empty_moov` enables MP4 fragmentation
clip.write_videofile(output_file_fragmented, codec="libx264", fps=24,
                     ffmpeg_params=['-movflags', 'frag_keyframe+empty_moov'])

print(f"Standard Video with metadata saved to {output_file}")
print(f"Fragmented MP4 Video with metadata saved to {output_file_fragmented}")
from moviepy.editor import ColorClip
import os
import subprocess

# Create a directory for the output if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple video clip
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=10)  # 10 seconds, red
clip_path = os.path.join(output_dir, 'simple_video.mp4')
clip.write_videofile(clip_path, fps=24)

# Define chapter metadata
chapters = [
    {
        'start': 0,
        'end': 3,
        'title': 'Chapter 1'
    },
    {
        'start': 3,
        'end': 6,
        'title': 'Chapter 2'
    },
    {
        'start': 6,
        'end': 9,
        'title': 'Chapter 3'
    }
]

# Prepare metadata for chapters in ffmpeg metadata format
metadata = ';'.join([f"[CHAPTER]\nTIMEBASE=1/1\nSTART={c['start']}\nEND={c['end']}\n"
                     f"title={c['title']}" for c in chapters])

# Content Description Tracks metadata
content_description = "This is a sample content description for indexing and content management."

# Write chapters and content description to a metadata file
metadata_file_path = os.path.join(output_dir, 'chapters_and_description.txt')
with open(metadata_file_path, 'w') as f:
    f.write(";FFMETADATA1\n")
    f.write(metadata + '\n')
    f.write(f"[COMMENTS]\ndescription={content_description}\n")

# Use subprocess to call ffmpeg directly to add the chapters and content description to the video
output_path = os.path.join(output_dir, 'video_with_chapters_and_description.mp4')
ffmpeg_command = [
    'ffmpeg',
    '-i', clip_path,
    '-i', metadata_file_path,
    '-map', '0',
    '-map_metadata', '1',
    '-codec', 'copy',
    '-f', 'mp4',
    output_path
]

# Execute the command
subprocess.run(ffmpeg_command, check=True)

# Cleanup temporary chapter metadata file
os.remove(metadata_file_path)
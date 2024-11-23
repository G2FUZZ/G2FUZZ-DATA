import os
from moviepy.editor import ColorClip
import ffmpeg

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple video using moviepy
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)
clip.write_videofile('./tmp/simple_video.mp4', fps=24)

# Define chapters
# Each chapter is defined by its start time, end time, and title.
# Times should be in milliseconds
chapters = [
    {'start_time': 0, 'end_time': 3000, 'title': 'Introduction'},
    {'start_time': 3000, 'end_time': 6000, 'title': 'Middle'},
    {'start_time': 6000, 'end_time': 10000, 'title': 'Conclusion'}
]

# Prepare metadata for chapters
metadata = []
for chapter in chapters:
    metadata.extend([
        '-metadata', f"chapter_start={chapter['start_time']}",
        '-metadata', f"chapter_end={chapter['end_time']}",
        '-metadata', f"title={chapter['title']}"
    ])

# Use ffmpeg to add chapters to the video
input_video_path = './tmp/simple_video.mp4'
output_video_path = './tmp/video_with_chapters.mp4'

ffmpeg.input(input_video_path).output(output_video_path, **{'map_metadata': 0, 'codec': 'copy'}, **{'metadata:g': metadata}).run()
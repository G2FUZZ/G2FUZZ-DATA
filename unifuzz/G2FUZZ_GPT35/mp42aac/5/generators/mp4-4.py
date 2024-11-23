import subprocess

# Create a simple mp4 file with chapter markers
output_file = "./tmp/chapters.mp4"

# Define the chapter markers (in seconds)
chapters = [
    {"name": "Chapter 1", "time": 0},
    {"name": "Chapter 2", "time": 10},
    {"name": "Chapter 3", "time": 20}
]

# Generate the ffmpeg command to create the mp4 file with chapters
ffmpeg_cmd = 'ffmpeg -y -f lavfi -i color=c=red:s=320x240:d=30 -c:v libx264 -t 30'
for chapter in chapters:
    chapter_time = chapter["time"] - sum([c["time"] for c in chapters[:chapters.index(chapter)]])
    ffmpeg_cmd += f' -metadata title="{chapter["name"]}" -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -t {chapter_time}'

ffmpeg_cmd += f' -c copy {output_file}'

# Execute the ffmpeg command
subprocess.run(ffmpeg_cmd, shell=True)
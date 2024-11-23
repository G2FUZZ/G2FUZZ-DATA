from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Create a simple video clip (solid color with dimensions and duration)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)

# Prepare a subtitle file (SRT)
srt_content = """1
00:00:00,000 --> 00:00:05,000
Hello, World!

2
00:00:05,000 --> 00:00:10,000
This is a test subtitle.
"""

with open('./tmp/subtitles.srt', 'w') as srt_file:
    srt_file.write(srt_content)

# Save the video (without subtitles), specifying fps
clip.write_videofile('./tmp/video.mp4', codec='libx264', fps=24)

# Use ffmpeg to add subtitles to the video file
# This step requires ffmpeg to be installed and accessible from the command line
os.system('ffmpeg -i ./tmp/video.mp4 -i ./tmp/subtitles.srt -c copy -c:s mov_text ./tmp/final_video_with_subtitles.mp4')

print("Video with subtitles has been saved to ./tmp/final_video_with_subtitles.mp4")
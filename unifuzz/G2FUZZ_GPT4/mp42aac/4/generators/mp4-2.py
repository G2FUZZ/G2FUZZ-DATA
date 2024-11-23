import cv2
import numpy as np
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip
import subprocess  # Import subprocess

# Parameters for the video
duration = 10  # seconds
width, height = 640, 480
fps = 24
background_color = (255, 0, 0)  # Red background
output_video_path = "./tmp/sample_video.mp4"
output_video_with_subs_path = "./tmp/sample_video_with_subs.mp4"
subtitle_file = "./tmp/subtitles.srt"

# Generate a simple video with MoviePy
def make_frame(t):
    # Create an image with background color
    img = np.ones((height, width, 3), dtype=np.uint8) * np.array(background_color, dtype=np.uint8)
    return img  # Return the frame for each t

clip = VideoClip(make_frame, duration=duration).set_fps(fps)

# Generate subtitles file
subtitles_content = """1
00:00:01,000 --> 00:00:03,000
Hello, this is the first subtitle.

2
00:00:04,000 --> 00:00:06,000
And here comes the second one.
"""

with open(subtitle_file, "w") as f:
    f.write(subtitles_content)

# Save the video
clip.write_videofile(output_video_path, fps=fps)

# Add subtitles to the video using ffmpeg command line
def add_subtitles_with_ffmpeg(video_path, subtitle_path, output_path):
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f"subtitles={subtitle_path}",
        '-codec:a', 'copy',  # Copy the audio stream without re-encoding
        output_path
    ]
    subprocess.run(cmd, check=True)

add_subtitles_with_ffmpeg(output_video_path, subtitle_file, output_video_with_subs_path)

print("Video with subtitles has been generated.")
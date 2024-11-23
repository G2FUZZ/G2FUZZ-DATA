import os
import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Duration of the video
duration = 10  # seconds

# Create a blank clip, for example, a color clip
color_clip = mp.ColorClip(size=(640, 480), color=(255, 0, 0), duration=duration)

# Define chapter markers (time in seconds, title)
chapters = [
    (0, 'Introduction'),
    (3, 'Chapter 1: The Beginning'),
    (6, 'Chapter 2: The Middle'),
    (9, 'Ending')
]

# Function to create matplotlib figure for a chapter
def make_frame(t):
    fig, ax = plt.subplots()
    chapter_titles = [title for start, title in chapters if start <= t]
    if chapter_titles:
        ax.text(0.5, 0.5, chapter_titles[-1], horizontalalignment='center',
                verticalalignment='center', transform=ax.transAxes, fontsize=15)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    return mplfig_to_npimage(fig)

# Create a video clip from the chapter markers
chapter_clip = mp.VideoClip(make_frame, duration=duration)

# Composite video with chapters on the color clip
final_clip = mp.CompositeVideoClip([color_clip, chapter_clip])

# Output file path
output_path = './tmp/with_chapter_markers.mp4'

# Write the video file with chapter markers
final_clip.write_videofile(output_path, fps=24)

# Inform about the video creation
print(f"Video with chapter markers has been saved to {output_path}")
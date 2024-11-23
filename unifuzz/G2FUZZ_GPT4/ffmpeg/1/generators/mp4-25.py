import os
import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt
import numpy as np
from cryptography.fernet import Fernet

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

# Define mood tracks (time in seconds, mood)
moods = [
    (0, 'Calm'),
    (3, 'Excited'),
    (6, 'Tense'),
    (9, 'Relieved')
]

# Function to create matplotlib figure for a chapter
def make_frame(t):
    fig, ax = plt.subplots()
    chapter_titles = [title for start, title in chapters if start <= t]
    mood_states = [mood for start, mood in moods if start <= t]
    text_str = chapter_titles[-1] if chapter_titles else ''
    if mood_states:
        text_str += '\nMood: ' + mood_states[-1]
    ax.text(0.5, 0.5, text_str, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=15)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    return mplfig_to_npimage(fig)

# Create a video clip from the chapter markers and mood tracks
chapter_mood_clip = mp.VideoClip(make_frame, duration=duration)

# Composite video with chapters and moods on the color clip
final_clip = mp.CompositeVideoClip([color_clip, chapter_mood_clip])

# Intermediate file path (unencrypted)
intermediate_path = './tmp/intermediate_with_chapter_mood_markers.mp4'

# Output file path (encrypted)
output_path = './tmp/encrypted_with_chapter_mood_markers.mp4'

# Write the intermediate video file (unencrypted)
final_clip.write_videofile(intermediate_path, fps=24)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the file
def encrypt_file(file_path, output_path, cipher_suite):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

# Encrypt the intermediate video file
encrypt_file(intermediate_path, output_path, cipher_suite)

# Inform about the video creation and encryption
print(f"Encrypted video with chapter and mood markers has been saved to {output_path}")
print(f"Encryption Key (keep this safe to decrypt the video): {key}")
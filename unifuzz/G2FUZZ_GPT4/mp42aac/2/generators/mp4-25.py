from moviepy.editor import VideoClip, AudioFileClip
from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create frame for each time t
def make_frame(t):
    fig, ax = plt.subplots()
    ax.clear()  # Clear previous frame
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # Example dynamic element: moving text
    ax.text(5, 5 + t, "Scalable Visualization with MPEG Surround Audio", fontsize=16, ha='center', va='center')
    ax.axis('off')  # Hide axes
    # Convert Matplotlib figure to image (numpy array)
    plt.close(fig)  # Close the figure to prevent memory leakage
    return mplfig_to_npimage(fig)

# Create a video clip from frames
clip = VideoClip(make_frame, duration=5)  # 5-second video

# Audio-related code
audio_path = os.path.join(output_dir, "audio_mpeg_surround.mp4")  # Assuming MPEG Surround audio is in an MP4 container

# Ensure the audio file exists. If not, print a warning and continue without audio.
if not os.path.isfile(audio_path):
    print(f"Warning: The audio file {audio_path} could not be found. The video will be generated without audio.")
    audio_clip = None
else:
    audio_clip = AudioFileClip(audio_file_path)

if audio_clip:
    clip = clip.set_audio(audio_clip)

# Save the video clip as an MP4 file with MPEG Surround audio
output_path = os.path.join(output_dir, "scalable_visualization_mpeg_surround.mp4")
clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec='aac')  # Using 'aac' as a placeholder; specific MPEG Surround support depends on the encoding library capabilities and may require a custom FFmpeg build or specific flags

print(f"Video saved at {output_path}")
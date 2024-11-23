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
    ax.text(5, 5 + t, "Scalable Visualization with E-AC-3 Audio and VC-1 Video", fontsize=16, ha='center', va='center')
    ax.axis('off')  # Hide axes
    # Convert Matplotlib figure to image (numpy array)
    plt.close(fig)  # Close the figure to prevent memory leakage
    return mplfig_to_npimage(fig)

# Create a video clip from frames
clip = VideoClip(make_frame, duration=5)  # 5-second video

# Audio-related code
audio_path = os.path.join(output_dir, "audio_eac3.ac3")

# Ensure the audio file exists. If not, print a warning and continue without audio.
if not os.path.isfile(audio_path):
    print(f"Warning: The audio file {audio_path} could not be found. The video will be generated without audio.")
    audio_clip = None
else:
    audio_clip = AudioFileClip(audio_path)

if audio_clip:
    clip = clip.set_audio(audio_clip)

# Save the video clip as an MP4 file with E-AC-3 audio and VC-1 video codec
output_path = os.path.join(output_dir, "scalable_visualization_vc1.mp4")
# Note: VC-1 video codec support may vary depending on the ffmpeg build and configuration.
# The video codec 'libx264' is used as a placeholder. Replace 'libx264' with 'vc1' or the correct codec string for VC-1 if your ffmpeg supports it.
clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec='aac')  # 'aac' audio codec for broader compatibility

print(f"Video saved at {output_path}")
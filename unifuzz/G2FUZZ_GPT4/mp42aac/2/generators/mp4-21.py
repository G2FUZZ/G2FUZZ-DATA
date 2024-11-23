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
    ax.text(5, 5 + t, "Scalable Visualization", fontsize=16, ha='center', va='center')
    ax.axis('off')  # Hide axes
    # Convert Matplotlib figure to image (numpy array)
    plt.close(fig)  # Close the figure to prevent memory leakage
    return mplfig_to_npimage(fig)

# Create a video clip from frames
clip = VideoClip(make_frame, duration=5)  # 5-second video

# Commenting out the audio-related code for testing purposes
# audio_path = os.path.join(output_dir, "audio_he_aac.aac")
# if not os.path.isfile(audio_path):
#     raise FileNotFoundError(f"The audio file {audio_path} could not be found. Please ensure it exists.")
# audio_clip = AudioFileClip(audio_path)
# clip = clip.set_audio(audio_clip)

# Save the video clip as an MP4 file without audio for testing
output_path = os.path.join(output_dir, "scalable_visualization.mp4")
clip.write_videofile(output_path, fps=24)  # Removed audio_codec='aac' since we're not including audio

print(f"Video saved at {output_path}")
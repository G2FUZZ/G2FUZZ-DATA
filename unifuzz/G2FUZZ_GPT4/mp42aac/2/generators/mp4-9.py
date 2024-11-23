from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):  # Corrected variable name here
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
    return mplfig_to_npimage(fig)

# Create a video clip from frames
clip = VideoClip(make_frame, duration=5)  # 5-second video

# Save the video clip as an MP4 file
output_path = os.path.join(output_dir, "scalable_visualization.mp4")
clip.write_videofile(output_path, fps=24)  # 24 frames per second

print(f"Video saved at {output_path}")
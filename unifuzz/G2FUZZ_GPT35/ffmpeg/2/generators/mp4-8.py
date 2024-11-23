import moviepy.editor as mp
import numpy as np

# Create a video clip with a black screen for 5 seconds
clip = mp.VideoClip(lambda t: np.zeros((480, 640, 3), dtype=np.uint8), duration=5)

# Save the video clip as an mp4 file
clip.write_videofile("./tmp/editable_feature.mp4", codec="libx264", fps=24)
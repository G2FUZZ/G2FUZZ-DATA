import moviepy.editor as mp
import numpy as np

# Create a video clip with a black screen for 10 seconds
clip = mp.VideoClip(make_frame=lambda t: np.zeros((720, 1280, 3)), duration=10)

# Write the video clip to an mp4 file
clip.write_videofile("./tmp/generated_video.mp4", codec="libx264", fps=24)
import moviepy.editor as mp
import numpy as np

# Create a video clip with a black screen for 5 seconds
clip = mp.VideoClip(make_frame=lambda t: np.zeros((720, 1280, 3), dtype=np.uint8), duration=5)

# Set the video clip's audio to None
clip = clip.set_audio(None)

# Save the video clip as an mp4 file in the tmp directory
clip.write_videofile("./tmp/blank_video.mp4", codec="libx264", fps=24)
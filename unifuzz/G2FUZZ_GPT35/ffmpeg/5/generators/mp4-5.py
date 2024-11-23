import moviepy.editor as mp
import numpy as np

# Create a video clip with high-quality content
clip = mp.VideoClip(make_frame=lambda t: np.array([255, 255, 255], dtype=np.uint8), duration=5)
clip.fps = 30
clip.size = (1920, 1080)

# Save the video clip as an mp4 file
clip.write_videofile("./tmp/high_quality_video.mp4", codec="libx264", fps=30)
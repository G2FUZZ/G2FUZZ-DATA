import numpy as np
import moviepy.editor as mp
from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt

def make_frame(t):
    if t < 0.5:
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(2 * np.pi * x * t)
        
        fig, ax = plt.subplots()
        ax.plot(x, y, color='red')
        ax.set_title('Interactive Plot')
        image = mplfig_to_npimage(fig)
        return image
    else:
        return np.zeros((1080, 1920, 3), dtype=np.uint8)

clip = mp.VideoClip(make_frame, duration=1)
clip.fps = 24  # Set the frames per second
clip.write_videofile("./tmp/interactive_video.mp4", codec="libx264", audio_codec="aac", bitrate="5M")
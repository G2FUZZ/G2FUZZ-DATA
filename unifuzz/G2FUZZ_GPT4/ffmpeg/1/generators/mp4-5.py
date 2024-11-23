import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# Configuration
duration = 5  # seconds
fps = 24  # frames per second

def make_frame(t):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Creating a 3D sine wave
    x = np.linspace(0, 1, 100)
    y = np.sin(2 * np.pi * (x - 0.01 * t))
    z = np.cos(2 * np.pi * (x - 0.01 * t))
    ax.plot3D(x, y, z)

    # Setting the viewing angle for the plot, which changes with time to create a rotating effect
    ax.view_init(elev=20, azim=int(360 * t / duration))

    # Hide axes
    ax.set_axis_off()

    # Convert Matplotlib figure to an RGB image and return it
    return mplfig_to_npimage(fig)

# Create a video clip
animation = VideoClip(make_frame, duration=duration)

# Save the video clip as an mp4 file
animation.write_videofile("./tmp/3d_graphics_animation.mp4", fps=fps)

print("Video saved successfully!")
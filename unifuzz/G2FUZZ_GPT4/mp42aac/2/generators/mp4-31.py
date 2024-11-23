import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import os
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data for a three-dimensional line
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi)
z = np.linspace(0, 1, 100)
line, = ax.plot(x, y, z)

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    return line,

def update(frame):
    ax.view_init(elev=10., azim=frame)
    return line,

# Creating the Animation object
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), init_func=init, blit=False)

# Save animation using MoviePy with compact file size settings
def make_frame(t):
    update(int(t*360/4))  # Update the plot to create rotation
    return mplfig_to_npimage(fig)  # Convert the matplotlib figure to a numpy array image

animation = VideoClip(make_frame, duration=4)  # Duration is in seconds

# For compact file size, we adjust the bitrate and opt for a lower resolution if necessary
animation.write_videofile("./tmp/3d_graphics_compact.mp4", fps=20, bitrate="500k", preset='medium')
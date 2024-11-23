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

# Save animation using MoviePy
def make_frame(t):
    update(int(t*360/4))  # Update the plot to create rotation
    return mplfig_to_npimage(fig)  # Convert the matplotlib figure to a numpy array image

animation = VideoClip(make_frame, duration=4)  # Duration is in seconds
animation.write_videofile("./tmp/3d_graphics.mp4", fps=20)  # fps = frames per second

# Code for generating 360-Degree Videos feature
# Note: The actual generation of a 360-degree video that can be used in VR is quite complex and 
# cannot be achieved directly through matplotlib and MoviePy as it requires a specific video format and metadata.
# This would typically involve capturing or rendering scenes in a 360-degree view and then using specialized 
# software or libraries to encode this into a format recognized by VR and 360-degree video players.
# However, you can simulate a 360-degree rotation by adjusting the view as we did above, but for a true 360-degree 
# video, you would need to integrate with other tools or software designed for VR content creation.
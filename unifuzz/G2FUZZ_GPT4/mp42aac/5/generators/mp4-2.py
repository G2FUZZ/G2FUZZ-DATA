import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the animation parameters
frames = 100
x = np.linspace(-5, 5, 100)

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot
line, = ax.plot([], [], [], lw=2)

# Set up the plot limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Animation update function
def update(frame):
    y = np.sin(x + 0.1 * frame)
    z = np.cos(x + 0.1 * frame)
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line,

# Create an animation
ani = FFMpegWriter(fps=20, metadata=dict(artist='Me'), bitrate=1800)
with ani.saving(fig, "./tmp/3d_graphics.mp4", 100):
    for i in range(frames):
        update(i)
        ani.grab_frame()
        plt.close('all')

print("MP4 file with 3D graphics has been saved to ./tmp/3d_graphics.mp4")